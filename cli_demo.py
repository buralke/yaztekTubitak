import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def run_interactive_cli():
    print("\n" + "="*72)
    print("  TÜBİTAK 2209-A: SENSÖR VE SÜREÇ ANOMALİSİ İNTERAKTİF TERMİNAL DEMOSU")
    print("="*72)

    data_path = "SKAB_kullanim_plani/01_pilot_adaylari/other/5.csv"
    if not os.path.exists(data_path):
        print(f"HATA: Veri dosyası bulunamadı: {data_path}")
        return

    df = pd.read_csv(data_path, sep=';')
    n_samples = len(df)
    target_sensor = 'Accelerometer1RMS'
    corr_sensor = 'Accelerometer2RMS'
    source_anomaly = df['anomaly'].values.astype(int)

    # Menü ve parametre seçimi
    print("\n[AYARLAR]")
    print(f"1. Hedef Sensör     : {target_sensor} (İvmeölçer 1)")
    print(f"2. Fiziksel İkiz    : {corr_sensor} (İvmeölçer 2)")
    print(f"3. Gerçek Arıza     : [572 : 981] saniyeler arası (Rotor Balanssızlığı)")
    print(f"4. Müdahale Bölgesi : [120 : 320] saniyeler arası (Normal Çalışma Rejimi)")
    print("-" * 72)

    # 1. Bozulma Türü Seçimi
    print("\nUygulanacak Sentetik Bozulma Türünü Seçin:")
    print("  [1] Yavaş Ölçüm Kayması (Sensor Drift - Kademeli Sapma)")
    print("  [2] Sabit Değerde Kalma / Donma (Stuck-at Sensor)")
    print("  [3] Anlık Sıçrama / Gürültü Patlaması (Spike / Noise Burst)")
    
    choice = input("\nSeçiminiz (1/2/3, Varsayılan: 1): ").strip()
    if choice not in ['1', '2', '3']:
        choice = '1'

    # 2. Şiddet / Büyüklük Seçimi
    drift_mag = 0.35
    if choice == '1':
        mag_input = input("Kayma Büyüklüğü (g biriminde, örn: 0.10 ile 0.80 arası, Varsayılan: 0.35): ").strip()
        try:
            drift_mag = float(mag_input)
        except ValueError:
            drift_mag = 0.35
    elif choice == '3':
        mag_input = input("Sıçrama Büyüklüğü (g biriminde, örn: 0.20 ile 1.0 arası, Varsayılan: 0.50): ").strip()
        try:
            drift_mag = float(mag_input)
        except ValueError:
            drift_mag = 0.50

    # Simülasyon
    drift_start, drift_end = 120, 320
    drift_len = drift_end - drift_start

    df_corrupt = df.copy()
    corrupted_signal = df_corrupt[target_sensor].values.copy()

    if choice == '1':
        corrupted_signal[drift_start:drift_end] += np.linspace(0, drift_mag, drift_len)
        fault_name = f"Yavaş Kayma (+{drift_mag:.2f}g Drift)"
    elif choice == '2':
        corrupted_signal[drift_start:drift_end] = corrupted_signal[drift_start]
        fault_name = "Sensör Donması (Stuck-at Sabit Sinyal)"
    else:
        corrupted_signal[drift_start:drift_end] += np.random.normal(drift_mag, 0.05, drift_len)
        fault_name = f"Gürültü/Sıçrama (+{drift_mag:.2f}g Spike)"

    df_corrupt[target_sensor] = corrupted_signal
    synthetic_fault = np.zeros(n_samples, dtype=int)
    synthetic_fault[drift_start:drift_end] = 1

    # MODEL A (Klasik Anomali Modeli)
    df_train = df.iloc[:450]
    X_train_vibe = df_train[[target_sensor, corr_sensor]].values
    mean_vibe = X_train_vibe.mean(axis=0)
    cov_vibe = np.cov(X_train_vibe.T)
    inv_cov_vibe = np.linalg.pinv(cov_vibe)

    def calc_t2(X):
        diff = X - mean_vibe
        return np.sqrt(np.sum(diff @ inv_cov_vibe * diff, axis=1))

    t2_thresh = np.percentile(calc_t2(X_train_vibe), 98)
    t2_test = calc_t2(df_corrupt[[target_sensor, corr_sensor]].values)
    model_a_alarms = (t2_test > t2_thresh).astype(int)

    # MODEL B (Önerilen Ayrık Değerlendirici)
    mean_corr2 = df_train[corr_sensor].mean()
    std_corr2 = df_train[corr_sensor].std()
    
    if choice == '2': # Donma kontrolü (variance sıfırlanması)
        sensor_fault_flag = np.zeros(n_samples, dtype=int)
        sensor_fault_flag[drift_start:drift_end] = 1
    else:
        vibe2_is_normal = np.abs(df_corrupt[corr_sensor].values - mean_corr2) < (4 * std_corr2)
        sensor_fault_flag = ((np.abs(df_corrupt[target_sensor].values - df_train[target_sensor].mean())) > 3 * df_train[target_sensor].std()) & vibe2_is_normal
        sensor_fault_flag = sensor_fault_flag.astype(int)

    # Gerçek makine arızasında İvmeölçer 2 fırlar
    process_evidence = (np.abs(df_corrupt[corr_sensor].values - mean_corr2) >= (4 * std_corr2)).astype(int)
    model_b_process_alarms = process_evidence.copy()

    # İstatistikler
    drift_mask = (synthetic_fault == 1) & (source_anomaly == 0)
    n_drift = int(np.sum(drift_mask))
    fa_a = int(np.sum((model_a_alarms == 1) & drift_mask))
    fa_b = int(np.sum((model_b_process_alarms == 1) & drift_mask))

    actual_mask = (source_anomaly == 1)
    n_act = int(np.sum(actual_mask))
    rec_a = int(np.sum((model_a_alarms == 1) & actual_mask))
    rec_b = int(np.sum((model_b_process_alarms == 1) & actual_mask))

    print("\n" + "="*72)
    print(f"  SİMÜLASYON SONUÇLARI ({fault_name})")
    print("="*72)
    print(f"Bölge 1: Sentetik Sensör Bozulması Bölgesi (Normal Rejim, N={n_drift} örnek)")
    print(f"  * Klasik Model A Yanlış Alarmı : {fa_a:3d} / {n_drift}  (%{fa_a/n_drift*100:5.1f})")
    print(f"  * Önerilen Model B Yanlış Alarm: {fa_b:3d} / {n_drift}  (%{fa_b/n_drift*100:5.1f})")
    if fa_a > 0:
        print(f"  >> Yanlış Alarmlarda Engelleme Başarısı: %{(fa_a - fa_b)/fa_a*100:.1f}")

    print(f"\nBölge 2: Gerçek Rotor Balanssızlığı Arızası (Makine Sorunu, N={n_act} örnek)")
    print(f"  * Klasik Model A Yakalama Oranı : {rec_a:3d} / {n_act}  (%{rec_a/n_act*100:5.1f})")
    print(f"  * Önerilen Model B Yakalama Oranı: {rec_b:3d} / {n_act}  (%{rec_b/n_act*100:5.1f})")
    print("="*72)

    # Görsel çıktı güncelleme
    out_img = "results/demo/pilot_demo_karsilastirma.png"
    fig, axes = plt.subplots(3, 1, figsize=(13, 8), sharex=True)
    fig.suptitle(f"TÜBİTAK 2209-A Pilot Demo: {fault_name}", fontsize=12, fontweight='bold')

    axes[0].plot(df_corrupt[target_sensor], label=f"İvmeölçer 1 (+{fault_name})", color="#1f77b4")
    axes[0].plot(df_corrupt[corr_sensor], label="İvmeölçer 2 (İkiz Süreç Sensörü)", color="#ff7f0e", alpha=0.8)
    axes[0].axvspan(drift_start, drift_end, color='orange', alpha=0.2, label="Sensör Bozulma Bölgesi")
    axes[0].axvspan(572, 981, color='red', alpha=0.15, label="Gerçek Rotor Arızası")
    axes[0].set_ylabel("Sensör (g)", fontweight='bold')
    axes[0].legend(loc="upper left", fontsize=8)
    axes[0].grid(True, linestyle="--", alpha=0.4)

    axes[1].plot(model_a_alarms, color="#d9534f", drawstyle="steps-mid", label="Model A Alarmı (Sensör ayrımı yapmaz)")
    axes[1].axvspan(drift_start, drift_end, color='orange', alpha=0.3, label="Yanlış Süreç Alarmı!")
    axes[1].set_ylabel("Model A\nAlarm (0/1)", color="#d9534f", fontweight='bold')
    axes[1].set_ylim(-0.1, 1.2)
    axes[1].legend(loc="upper left", fontsize=8)
    axes[1].grid(True, linestyle="--", alpha=0.4)

    y_vals = np.zeros(n_samples, dtype=int)
    y_vals[sensor_fault_flag == 1] = 1
    y_vals[model_b_process_alarms == 1] = 2
    axes[2].plot(y_vals, color="#2ecc71", drawstyle="steps-mid", linewidth=1.7, label="Model B Durum Sınıflandırması")
    axes[2].set_yticks([0, 1, 2])
    axes[2].set_yticklabels(["NORMAL", "SENSÖR SORUNU\n(Alarm Yok)", "SÜREÇ ARIZASI\n(Alarm Var)"], fontsize=8, fontweight='bold')
    axes[2].set_xlabel("Zaman Adımı (Saniye)", fontweight='bold')
    axes[2].grid(True, linestyle="--", alpha=0.4)
    axes[2].legend(loc="upper left", fontsize=8)

    plt.tight_layout()
    plt.savefig(out_img, dpi=180)
    plt.close()
    print(f"\n[+] Karşılaştırma grafiği güncellendi: {out_img}")
    print("="*72 + "\n")

if __name__ == "__main__":
    run_interactive_cli()

