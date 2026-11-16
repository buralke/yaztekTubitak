import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_graphical_abstract():
    # 300 DPI profesyonel yayın ve rapor kalitesi
    fig, ax = plt.subplots(figsize=(15, 9), dpi=300)
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 9)
    ax.axis('off')

    # Renk Paleti (Modern Akademik / Endüstriyel)
    c_bg_box = "#f8fafc"
    c_border = "#94a3b8"
    c_input = "#e0f2fe"     # Açık mavi
    c_input_b = "#0284c7"
    c_corrupt = "#ffedd5"   # Açık turuncu
    c_corrupt_b = "#ea580c"
    c_layer1 = "#fef3c7"    # Açık sarı
    c_layer1_b = "#d97706"
    c_layer2 = "#ede9fe"    # Açık mor
    c_layer2_b = "#7c3aed"
    c_norm = "#dcfce7"      # Yeşil
    c_norm_b = "#16a34a"
    c_sensor = "#fef9c3"    # Sarı/Turuncu
    c_sensor_b = "#ca8a04"
    c_proc = "#fee2e2"      # Kırmızı
    c_proc_b = "#dc2626"
    c_dual = "#f1f5f9"      # Nötr koyu
    c_dual_b = "#475569"

    # Başlık Alanı
    ax.text(7.5, 8.55, "ÇİFT KADEMELİ SENSÖR GÜVENİLİRLİĞİ VE SÜREÇ ANOMALİSİ DEĞERLENDİRME ÇERÇEVESİ",
            ha='center', va='center', fontsize=14, fontweight='bold', color='#0f172a')
    ax.text(7.5, 8.25, "TÜBİTAK 2209-A: Eksik ve Bozulmuş Endüstriyel Sensör Verilerinde Yanlış Alarm Azaltma Akış Şeması (Graphical Abstract)",
            ha='center', va='center', fontsize=10, fontstyle='italic', color='#475569')

    # ==========================================
    # SÜTUN 1: GİRDİ VE BOZULMA (0.5 - 3.8)
    # ==========================================
    box_s1 = patches.FancyBboxPatch((0.5, 0.6), 3.4, 7.3, boxstyle="round,pad=0.2",
                                    facecolor=c_bg_box, edgecolor=c_border, linestyle='--', linewidth=1.5)
    ax.add_patch(box_s1)
    ax.text(2.2, 7.6, "1. GÖZLEM VE BOZULMA", ha='center', va='center', fontsize=11, fontweight='bold', color='#1e293b')

    # Ham Veri Kutusu
    b_raw = patches.FancyBboxPatch((0.7, 5.2), 3.0, 2.0, boxstyle="round,pad=0.1",
                                   facecolor=c_input, edgecolor=c_input_b, linewidth=1.5)
    ax.add_patch(b_raw)
    ax.text(2.2, 6.7, "SKAB Testbed Veri Kümesi", ha='center', va='center', fontsize=10, fontweight='bold', color='#0369a1')
    ax.text(2.2, 6.2, "• 8 Endüstriyel Sensör (1 Hz)\n  (Titreşim 1-2, Akım, Basınç,\n   Sıcaklık, Debi, Gerilim)\n• 35 Çok Değişkenli CSV Serisi", 
            ha='center', va='center', fontsize=8.5, color='#0f172a')

    # Sentetik Bozulma Motoru
    b_corrupt = patches.FancyBboxPatch((0.7, 1.2), 3.0, 3.4, boxstyle="round,pad=0.1",
                                       facecolor=c_corrupt, edgecolor=c_corrupt_b, linewidth=1.5)
    ax.add_patch(b_corrupt)
    ax.text(2.2, 4.15, "Kontrollü Bozulma Motoru", ha='center', va='center', fontsize=10, fontweight='bold', color='#c2410c')
    ax.text(2.2, 3.9, "(Ham veriyi bozmadan bellek içi)", ha='center', va='center', fontsize=7.5, fontstyle='italic', color='#9a3412')
    ax.text(2.2, 2.7, "• Yavaş Ölçüm Kayması (Drift)\n  (1-sigma ile 5-sigma arası)\n• Sinyal Donması (Stuck-at)\n• Gürültü Sıçraması (Spike)\n• Ardışık Ölçüm Kaybı (Gaps)\n\n[Hedef Sensör: Tekil Kanal]", 
            ha='center', va='center', fontsize=8.5, color='#431407')

    # Ok: Ham Veriden Bozulmaya
    ax.annotate('', xy=(2.2, 4.6), xytext=(2.2, 5.2),
                arrowprops=dict(arrowstyle="->", color=c_corrupt_b, lw=2))

    # ==========================================
    # SÜTUN 2: ÇİFT KADEMELİ KARAR MOTORU (4.6 - 9.8)
    # ==========================================
    box_s2 = patches.FancyBboxPatch((4.5, 0.6), 5.4, 7.3, boxstyle="round,pad=0.2",
                                    facecolor=c_bg_box, edgecolor=c_border, linestyle='--', linewidth=1.5)
    ax.add_patch(box_s2)
    ax.text(7.2, 7.6, "2. ÇİFT KADEMELİ AYRIŞTIRMA MİMARİSİ", ha='center', va='center', fontsize=11, fontweight='bold', color='#1e293b')

    # Kademe 1: Sensör Güvenilirlik Katmanı
    b_k1 = patches.FancyBboxPatch((4.8, 4.4), 4.8, 2.8, boxstyle="round,pad=0.1",
                                  facecolor=c_layer1, edgecolor=c_layer1_b, linewidth=1.5)
    ax.add_patch(b_k1)
    ax.text(7.2, 6.8, "Kademe 1: Sensör Tutarlılık Katmanı", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#b45309')
    ax.text(7.2, 6.45, "Çapraz Sensör Fiziksel Artık (Residual) Analizi", ha='center', va='center', fontsize=8.5, fontweight='semibold', color='#78350f')
    ax.text(7.2, 5.45, "• Fiziksel olarak korele ikiz sensörler izlenir\n  (Örn: Motor milindeki İvmeölçer 1 vs İvmeölçer 2)\n• Hedef sensör saparken ikiz sensör sakin mi?\n  -> EVET: 'Sensör Bozulması' Bayrağı\n  -> HAYIR: 'Sensör Sağlam / Ortak Hareket'", 
            ha='center', va='center', fontsize=8.5, color='#451a03')

    # Kademe 2: Süreç Anomalisi Değerlendirme Katmanı
    b_k2 = patches.FancyBboxPatch((4.8, 1.0), 4.8, 2.9, boxstyle="round,pad=0.1",
                                  facecolor=c_layer2, edgecolor=c_layer2_b, linewidth=1.5)
    ax.add_patch(b_k2)
    ax.text(7.2, 3.5, "Kademe 2: Süreç Anomalisi Katmanı", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#6d28d9')
    ax.text(7.2, 3.15, "Şüpheli Kanal İzolasyonu & Çok Değişkenli Takip", ha='center', va='center', fontsize=8.5, fontweight='semibold', color='#4c1d95')
    ax.text(7.2, 2.15, "• Şüpheli sensör dışlanarak kalan güvenilir kanallar alınır\n• Mahalanobis Mesafesi & İzolasyon Ormanı\n• Çoklu süreç kanıtı var mı?\n  -> EVET: 'Gerçek Süreç Anomalisi Alarmı'\n  -> HAYIR: 'Süreç Normal (Yanlış Alarm Yok)'", 
            ha='center', va='center', fontsize=8.5, color='#2e1065')

    # Ok: Girdiden Kademe 1'e
    ax.annotate('', xy=(4.8, 5.8), xytext=(3.7, 3.5),
                arrowprops=dict(arrowstyle="->", color='#2563eb', lw=2, connectionstyle="arc3,rad=-0.15"))
    ax.text(4.1, 4.9, "Sinyal Akışı", fontsize=8, fontweight='bold', color='#2563eb', rotation=30)

    # Ok: Kademe 1'den Kademe 2'ye (Kanal Kontrolü)
    ax.annotate('', xy=(7.2, 3.9), xytext=(7.2, 4.4),
                arrowprops=dict(arrowstyle="->", color=c_layer1_b, lw=2))
    ax.text(7.25, 4.15, "Güvenilirlik Skoru & Kanal Maskesi", fontsize=8, color='#92400e', va='center')

    # ==========================================
    # SÜTUN 3: 4 DURUMLU ÇIKTI MATRİSİ (10.5 - 14.5)
    # ==========================================
    box_s3 = patches.FancyBboxPatch((10.5, 0.6), 4.0, 7.3, boxstyle="round,pad=0.2",
                                    facecolor=c_bg_box, edgecolor=c_border, linestyle='--', linewidth=1.5)
    ax.add_patch(box_s3)
    ax.text(12.5, 7.6, "3. HEDEF ÇIKTI MATRİSİ", ha='center', va='center', fontsize=11, fontweight='bold', color='#1e293b')

    # Durum 1: NORMAL
    b_d1 = patches.FancyBboxPatch((10.7, 6.0), 3.6, 1.25, boxstyle="round,pad=0.08",
                                  facecolor=c_norm, edgecolor=c_norm_b, linewidth=1.5)
    ax.add_patch(b_d1)
    ax.text(12.5, 6.85, "DURUM 1: NORMAL", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#15803d')
    ax.text(12.5, 6.35, "Süreç Normal + Sensör Sağlam\n(Sistem kararlı rejimde)", ha='center', va='center', fontsize=8, color='#14532d')

    # Durum 2: SENSÖR SORUNU (Önemli Yenilik)
    b_d2 = patches.FancyBboxPatch((10.7, 4.4), 3.6, 1.35, boxstyle="round,pad=0.08",
                                  facecolor=c_sensor, edgecolor=c_sensor_b, linewidth=2.0)
    ax.add_patch(b_d2)
    ax.text(12.5, 5.35, "DURUM 2: YALNIZ SENSÖR SORUNU", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#a16207')
    ax.text(12.5, 4.8, "Süreç Normal + Sensör Bozulmuş\n★ YANLIŞ ALARM ENGELLENDİ ★\n(Bakım uyarısı verilir, makine durdurulmaz)", ha='center', va='center', fontsize=7.5, fontweight='semibold', color='#713f12')

    # Durum 3: SÜREÇ ANOMALİSİ
    b_d3 = patches.FancyBboxPatch((10.7, 2.8), 3.6, 1.25, boxstyle="round,pad=0.08",
                                  facecolor=c_proc, edgecolor=c_proc_b, linewidth=1.5)
    ax.add_patch(b_d3)
    ax.text(12.5, 3.65, "DURUM 3: SÜREÇ ANOMALİSİ", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#b91c1c')
    ax.text(12.5, 3.15, "Gerçek Makine / Süreç Arızası\n(Alarm tetiklenir, yüksek hassasiyet)", ha='center', va='center', fontsize=8, color='#7f1d1d')

    # Durum 4: ÇİFT SORUN
    b_d4 = patches.FancyBboxPatch((10.7, 1.2), 3.6, 1.25, boxstyle="round,pad=0.08",
                                  facecolor=c_dual, edgecolor=c_dual_b, linewidth=1.5)
    ax.add_patch(b_d4)
    ax.text(12.5, 2.05, "DURUM 4: ÇİFT SORUN", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#334155')
    ax.text(12.5, 1.55, "Süreç Arızası + Sensör Bozuk\n(Kritik arıza alarmı + sensör uyarısı)", ha='center', va='center', fontsize=8, color='#1e293b')

    # Oklar: Kademe 1 ve 2'den Çıktılara
    ax.annotate('', xy=(10.7, 6.6), xytext=(9.6, 5.8),
                arrowprops=dict(arrowstyle="->", color='#16a34a', lw=1.5))
    ax.annotate('', xy=(10.7, 5.1), xytext=(9.6, 5.3),
                arrowprops=dict(arrowstyle="->", color='#ca8a04', lw=2))
    ax.annotate('', xy=(10.7, 3.4), xytext=(9.6, 2.5),
                arrowprops=dict(arrowstyle="->", color='#dc2626', lw=1.5))
    ax.annotate('', xy=(10.7, 1.8), xytext=(9.6, 2.0),
                arrowprops=dict(arrowstyle="->", color='#475569', lw=1.5))

    # Alt Bilgi Notu
    ax.text(7.5, 0.25, "Gözlem Yetersizliği / Aşırı Veri Kaybı Durumunda Sistem Otomatik Olarak 'DEĞERLENDİRİLEMİYOR' Durum Çıktısı Üretir.",
            ha='center', va='center', fontsize=8.5, fontweight='bold', color='#475569')

    plt.tight_layout()
    out_path = 'results/demo/graphical_abstract.png'
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Graphical Abstract başarıyla üretildi: {out_path}")

if __name__ == '__main__':
    draw_graphical_abstract()

