import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Grafikler için temiz, şık ve endüstriyel görselleştirme stili
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 0.8

# Sensör bilgileri ve fiziksel birimleri (README doğrulamalı)
SENSOR_INFO = [
    ("Accelerometer1RMS", "İvmeölçer 1 RMS (g)", "#1f77b4"),
    ("Accelerometer2RMS", "İvmeölçer 2 RMS (g)", "#ff7f0e"),
    ("Current", "Motor Akımı (A)", "#2ca02c"),
    ("Pressure", "Pompa Çıkış Basıncı (bar)", "#d62728"),
    ("Temperature", "Motor Gövde Sıcaklığı (°C)", "#9467bd"),
    ("Thermocouple", "Sirkülasyon Sıvı Sıcaklığı (°C)", "#8c564b"),
    ("Voltage", "Motor Gerilimi (V)", "#e377c2"),
    ("Volume Flow RateRMS", "Sirkülasyon Debi RMS (L/dk)", "#17becf")
]

def plot_experiment(csv_path, exp_name, description, output_path):
    df = pd.read_csv(csv_path, sep=';')
    df['datetime'] = pd.to_datetime(df['datetime'])
    
    fig, axes = plt.subplots(len(SENSOR_INFO), 1, figsize=(14, 16), sharex=True)
    fig.suptitle(f"SKAB Deney İncelemesi: {exp_name}\nAçıklama: {description}", 
                 fontsize=14, fontweight='bold', y=0.995)
    
    has_anomaly = 'anomaly' in df.columns
    has_changepoint = 'changepoint' in df.columns
    
    # Anomali aralıklarını bul (ardışık bloklar)
    anomaly_spans = []
    if has_anomaly:
        is_anom = df['anomaly'].values
        in_span = False
        start_idx = None
        for i, val in enumerate(is_anom):
            if val == 1.0 and not in_span:
                in_span = True
                start_idx = i
            elif val == 0.0 and in_span:
                in_span = False
                anomaly_spans.append((df['datetime'].iloc[start_idx], df['datetime'].iloc[i-1]))
        if in_span:
            anomaly_spans.append((df['datetime'].iloc[start_idx], df['datetime'].iloc[-1]))

    # Değişim noktaları
    cp_times = []
    if has_changepoint:
        cp_times = df[df['changepoint'] == 1.0]['datetime'].tolist()

    for idx, (col_name, label, color) in enumerate(SENSOR_INFO):
        ax = axes[idx]
        ax.plot(df['datetime'], df[col_name], color=color, linewidth=1.2, label=col_name)
        ax.set_ylabel(label, fontsize=9, fontweight='semibold')
        ax.grid(True, linestyle='--', alpha=0.5)
        
        # Anomali aralıklarını boya
        for start_dt, end_dt in anomaly_spans:
            ax.axvspan(start_dt, end_dt, color='#ff4d4d', alpha=0.2, 
                       label='Kaynak Anomali Aralığı (anomaly=1)' if idx == 0 else "")
            
        # Değişim noktalarını çiz
        for cp_dt in cp_times:
            ax.axvline(cp_dt, color='#111111', linestyle=':', linewidth=1.5,
                       label='Değişim Noktası (changepoint=1)' if idx == 0 and cp_dt == cp_times[0] else "")
            
        if idx == 0:
            # Sadece ilk grafikte legend göster
            handles, labels = ax.get_legend_handles_labels()
            by_label = dict(zip(labels, handles))
            ax.legend(by_label.values(), by_label.keys(), loc='upper right', framealpha=0.9, fontsize=8)

    axes[-1].set_xlabel("Zaman Damgası (datetime)", fontsize=10, fontweight='semibold')
    axes[-1].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    fig.autofmt_xdate()
    plt.tight_layout()
    plt.subplots_adjust(top=0.94)
    plt.savefig(output_path, dpi=200, bbox_inches='tight')
    plt.close()
    print(f"Grafik kaydedildi: {output_path}")

def main():
    experiments = [
        {
            "path": "SKAB/data/raw/SKAB/data/valve1/1.csv",
            "name": "valve1/1 (Pompa Giriş Vanası Kapatma)",
            "desc": "Pompa emiş vanasının kademeli/ani kısılması ile oluşan akış kaybı ve basınç düşüşü simülasyonu",
            "out": "results/data_review/experiment_valve1_1.png"
        },
        {
            "path": "SKAB/data/raw/SKAB/data/other/5.csv",
            "name": "other/5 (Rotor Balanssızlığı - Ani Davranış)",
            "desc": "Rotor mekanik dengesizliğinin aniden devreye girmesi, titreşim ivmeölçerlerinde belirgin sapma",
            "out": "results/data_review/experiment_other_5.png"
        },
        {
            "path": "SKAB/data/raw/SKAB/data/other/13.csv",
            "name": "other/13 (Pompa Girişinde İki Fazlı Akış / Kavitasyon)",
            "desc": "Sıvı hattına hava/buhar karışımı verilerek kavitasyon ortamı oluşturulması ve hidrolik düzensizlik",
            "out": "results/data_review/experiment_other_13.png"
        },
        {
            "path": "SKAB/data/raw/SKAB/data/anomaly-free/anomaly-free.csv",
            "name": "anomaly-free/anomaly-free (Normal Çalışma Rejimi - İlk 1200 Örnek)",
            "desc": "Hiçbir müdahale yapılmamış normal referans çalışma koşulu (karşılaştırma amacıyla)",
            "out": "results/data_review/experiment_anomaly_free.png",
            "is_anomaly_free": True
        }
    ]
    
    for exp in experiments:
        if exp.get("is_anomaly_free"):
            # Anomaly-free çok uzun (9405 satır), ilk 1200 saniyelik kısmını veya tamamını çizelim
            df = pd.read_csv(exp["path"], sep=';')
            df['datetime'] = pd.to_datetime(df['datetime'])
            df_subset = df.iloc[:1500].copy()
            
            fig, axes = plt.subplots(len(SENSOR_INFO), 1, figsize=(14, 16), sharex=True)
            fig.suptitle(f"SKAB Deney İncelemesi: {exp['name']}\nAçıklama: {exp['desc']}", 
                         fontsize=14, fontweight='bold', y=0.995)
            
            for idx, (col_name, label, color) in enumerate(SENSOR_INFO):
                ax = axes[idx]
                ax.plot(df_subset['datetime'], df_subset[col_name], color=color, linewidth=1.2)
                ax.set_ylabel(label, fontsize=9, fontweight='semibold')
                ax.grid(True, linestyle='--', alpha=0.5)
                
            axes[-1].set_xlabel("Zaman Damgası (datetime)", fontsize=10, fontweight='semibold')
            axes[-1].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
            fig.autofmt_xdate()
            plt.tight_layout()
            plt.subplots_adjust(top=0.94)
            plt.savefig(exp["out"], dpi=200, bbox_inches='tight')
            plt.close()
            print(f"Grafik kaydedildi: {exp['out']}")
        else:
            plot_experiment(exp["path"], exp["name"], exp["desc"], exp["out"])

if __name__ == "__main__":
    main()
