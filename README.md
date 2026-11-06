# 🧭 Proje Haritası ve Kullanım Kılavuzu (Project Map & Guide)

Bu doküman, **Endüstriyel Sensör Verilerinde Sensör Hatası ile Süreç Anomalisinin Ayrı Değerlendirilmesi** (TÜBİTAK 2209-A) projesinin dizin yapısını, üretilen raporları, veri setlerini ve pilot demo araçlarının kullanım adımlarını içerir.

> 💡 **İpucu:** Aşağıdaki mavi bağlantılara tıklayarak doğrudan ilgili klasörlere, veri setlerine veya kod dosyalarına gidebilirsiniz.

---

## 🗺️ 1. Proje Dizin Haritası (Folder Map)

```text
yaztekEndustriyelSensorProjesi/
├── 📁 SKAB_kullanim_plani/         --> Kullanım amaçlarına göre ayrılmış ve doğrulanmış SKAB verileri
│   ├── 📁 00_belgeler/            --> Kaynak SKAB README ve GPL-3.0 lisans dosyaları
│   ├── 📁 01_pilot_adaylari/      --> İlk pilot çalışma için seçilen vana ve rotor deneyleri
│   ├── 📁 02_normal_referans_adayi/-> Müdahalesiz referans çalışma serisi (anomaly-free)
│   ├── 📁 03_zaman_boslugu_degerlendirmesi/ -> Zaman atlaması (dt > 2s) içeren 7 deney
│   ├── 📁 04_diger_deney_adaylari/ -> İleride kullanılacak yedek 25 deney serisi
│   ├── 📁 05_inceleme_bekleyenler/ -> Tutarsızlık/hata tespit edilen dosyalar (Şu an 0 adet)
│   ├── 📁 06_grafikler_ve_raporlar/-> Envanter tabloları, veri raporları ve analiz grafikleri
│   ├── 📄 manifest.csv             --> 35 CSV dosyasının meta veri ve kullanım grubu dökümü
│   ├── 📄 copy_verification.csv    --> SHA-256 hash ve bayt boyutu doğrulama tablosu
│   └── 📄 README.md                --> Veri organizasyonunun detaylı dokümantasyonu
│
├── 📁 cikti/                       --> Veri inceleme ve pilot değerlendirme raporları
│   ├── 📄 skab_veri_inceleme_ciktisi.md
│   └── 📄 SKAB Veri İnceleme Raporunun Değerlendirilmesi ve İlk Pilot Kararları.md
│
├── 📁 docs/                        --> Metodolojik kararlar ve veri uygunluk analizleri
│   ├── 📄 dataset_review.md        --> Veri uygunluğu, fiziksel sınırlar ve kanıt kapsamı
│   └── 📄 decisions.md             --> Proje terminolojisi ve mimari kararlar günlüğü
│
├── 📁 results/                     --> Görselleştirmeler, envanter ve demo çıktıları
│   ├── 📁 data_review/             --> inventory.csv, column_quality.csv ve ilk deney grafikleri
│   └── 📁 demo/                    --> Pilot demo karşılaştırma grafikleri ve veri dosyaları
│       ├── 📄 pilot_demo_karsilastirma.png --> Klasik model ile önerilen modelin karşılaştırma grafiği
│       ├── 📄 demo_data.json       --> Demo zaman serisi sayısal verileri
│       └── 📄 index.html           --> İnteraktif web dashboard arayüzü
│
├── 📁 pdf's/                       --> TÜBİTAK 2209-A başvuru taslağı ve karar metni PDF'leri
├── 📁 prompts/                     --> Ajan ve geliştirme promptları
│
├── 🐍 pilot_demo.py                --> Otomatik çalışan pilot analiz betiği (Rotor Titreşimi Üzerinde)
├── 🐍 cli_demo.py                  --> Terminal üzerinden etkileşimli çalışan parametrik demo betiği
├── 🐍 plot_experiments.py          --> Temsili deneylerin zaman serisi grafiklerini çizen betik
└── 🐍 src_inspect.py               --> 35 CSV'yi tarayıp inventory.csv üreten inceleme betiği
```

---

## 📂 2. Doğrudan Klasör ve Dosya Bağlantıları

Aşağıdaki bağlantılara tıklayarak dosya sisteminde doğrudan ilgili konuma ulaşabilirsiniz:

* 📂 [SKAB Kullanım Planı Klasörü](SKAB_kullanim_plani/)
  * 📂 [01. Pilot Adayları (valve1/1 ve other/5)](SKAB_kullanim_plani/01_pilot_adaylari/)
  * 📂 [02. Normal Referans Serisi (anomaly-free)](SKAB_kullanim_plani/02_normal_referans_adayi/)
  * 📂 [03. Zaman Boşluğu İçeren Deneyler](SKAB_kullanim_plani/03_zaman_boslugu_degerlendirmesi/)
  * 📂 [04. Diğer Deney Havuzu (25 CSV)](SKAB_kullanim_plani/04_diger_deney_adaylari/)
  * 📂 [06. Rapor ve Grafik Arşivi](SKAB_kullanim_plani/06_grafikler_ve_raporlar/)
  * 📊 [manifest.csv (Meta Veri Listesi)](SKAB_kullanim_plani/manifest.csv)
  * 🔒 [copy_verification.csv (Kriptografik SHA-256 Tablosu)](SKAB_kullanim_plani/copy_verification.csv)
* 📂 [Çıktılar Klasörü (Raporlar)](cikti/)
  * 📝 [skab_veri_inceleme_ciktisi.md](cikti/skab_veri_inceleme_ciktisi.md)
  * 📝 [SKAB Veri İnceleme Raporunun Değerlendirilmesi ve İlk Pilot Kararları.md](cikti/SKAB%20Veri%20İnceleme%20Raporunun%20Değerlendirilmesi%20ve%20İlk%20Pilot%20Kararları.md)
* 📂 [Dokümantasyon Klasörü (docs)](docs/)
  * 📘 [dataset_review.md (Veri Uygunluk Raporu)](docs/dataset_review.md)
  * 📙 [decisions.md (Karar Günlüğü & Terminoloji)](docs/decisions.md)
* 📂 [Sonuçlar Klasörü (results)](results/)
  * 🖼️ [pilot_demo_karsilastirma.png (Demo Karşılaştırma Grafiği)](results/demo/pilot_demo_karsilastirma.png)
  * 🌐 [index.html (İnteraktif Web Dashboard Dosyası)](results/demo/index.html)
* 📂 [PDF Belgeleri Klasörü](pdf's/)
* 📂 [Prompt Belgeleri Klasörü](prompts/)

---

## 🚀 3. Pilot Demoları Çalıştırma Kılavuzu

Projemizde iki farklı demo aracı bulunmaktadır:

### A) Terminal Üzerinden Etkileşimli Demo ([`cli_demo.py`](cli_demo.py))
Bu araç, terminal ortamında klavyeden bozulma türü ve şiddeti seçerek anlık yanlış alarm oranlarını incelemenizi sağlar.

**Çalıştırma:**
```powershell
python cli_demo.py
```
1. **Bozulma Türü Seçimi:**
   * `[1]` Yavaş Ölçüm Kayması (Sensor Drift - Kademeli artış)
   * `[2]` Sensör Sinyalinin Donması (Stuck-at - Sabit kalma)
   * `[3]` Anlık Sıçrama / Gürültü Patlaması (Spike)
2. **Kayma Büyüklüğü:**
   * Örneğin `0.35` yazıp Enter'a basabilirsiniz.
3. **Çıktı:** Sayısal başarı tablosu ekrana yazdırılır ve [`results/demo/pilot_demo_karsilastirma.png`](results/demo/pilot_demo_karsilastirma.png) grafiği anında güncellenir.

---

### B) Otomatik Pilot Deney Betiği ([`pilot_demo.py`](pilot_demo.py))
Tüm hesaplamaları standart parametrelerle baştan sona yürüten betiktir.
```powershell
python pilot_demo.py
```

---

### C) İnteraktif Web Arayüzü ([`results/demo/index.html`](results/demo/index.html))
Tarayıcı üzerinden kaydırıcılar (slider) ile görsel test yapmak isterseniz:
1. Terminalden mini web sunucusunu başlatın:
   ```powershell
   python -m http.server 8050 --directory results/demo
   ```
2. Tarayıcınızda açın: **http://localhost:8050**
3. İşi bitince terminalden `Ctrl + C` tuşlayarak sunucuyu kapatabilirsiniz.

---

## 🔬 4. Metodolojik Çerçeve ve Temel Ayrım

* **Süreç Anomalisi:** Makinenin veya sistemin fiziksel çalışmasındaki sapma (örn. rotor dengesizliği veya vana tıkanması).
* **Sensör/Veri Hatası:** Ölçüm cihazı veya iletim kaynaklı bozulma (kayma, donma, gürültü, paket kaybı).
* **Temel Prensip:** Gerçek bir makine arızasında birbirine fiziksel olarak bağlı sensörler (örn. motor milindeki iki titreşim ivmeölçeri) birlikte hareket eder. Ancak bir sensör tek başına kayarken diğeri normal kalıyorsa, sistem bunu **"Süreç Anomalisi Değil, Sensör Bozulması"** olarak ayrıştırır ve gereksiz fabrika duruş alarmlarını önler.

