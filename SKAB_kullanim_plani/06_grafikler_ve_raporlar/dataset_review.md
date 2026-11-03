# SKAB Veri Seti İnceleme ve Uygunluk Raporu (Dataset Review)

**Rapor Tarihi:** 28 Ekim 2026  
**İlgili Proje:** Endüstriyel Sensör Verilerinde Sensör Sorunu ve Süreç Anomalisinin Ayrı Değerlendirilmesi (TÜBİTAK 2209-A Taslağı)  
**Referans Belgeler:**  
- `pdf's/26.10.2026.pdf` (Araştırma ve Yazılım Tasarımı Karar Metni)  
- `pdf's/2209A_03_Endustriyel_Sensor_Detayli_Taslak_Makaleli-2.pdf` (TÜBİTAK 2209-A Taslak Metni)  
- `SKAB/data/raw/SKAB/README.md` ve `SKAB/data/raw/SKAB/data/README.md`  

---

## 1. Veri Kaynağı, Fiziksel Sistem ve Kapsam

### 1.1. Fiziksel Test Düzeneği (Testbed)
Skoltech Anomaly Benchmark (SKAB), Skoltech bünyesindeki kapalı devre su sirkülasyon test düzeneğinden toplanmış endüstriyel çok değişkenli zaman serilerinden oluşmaktadır. Sistem şu fiziksel bileşenleri barındırmaktadır:
- Elektrikli su pompası ve tahrik motoru
- Kapalı su sirkülasyon döngüsü (borular, tank ve vanalar)
- Giriş kontrol vanası (Valve 1) ve çıkış kontrol vanası (Valve 2)
- Mekanik balanssızlık ekleme mekanizması (rotor şaftı)
- 8 adet fiziksel sensör (2 titreşim ivmeölçeri, akım, gerilim, pompa çıkış basıncı, motor gövde sıcaklığı, akışkan termokupl sıcaklığı, hacimsel akış debisi).

### 1.2. Dosya ve Dizin Yapısı
Veriler çalışma alanında `SKAB/data/raw/SKAB/` altında konumlanmıştır:
```text
SKAB/data/raw/SKAB/
├── data/
│   ├── anomaly-free/
│   │   └── anomaly-free.csv       # Müdahalesiz normal çalışma referansı (9.405 satır)
│   ├── valve1/                    # Pompa giriş vanası kapatma deneyleri (16 CSV dosyası)
│   ├── valve2/                    # Pompa çıkış vanası kapatma deneyleri (4 CSV dosyası)
│   └── other/                     # Diğer süreç anomalisi deneyleri (14 CSV dosyası)
│       ├── 1.csv - 4.csv          # Sıvı sızıntısı ve sıvı ekleme simülasyonları
│       ├── 5.csv - 9.csv          # Rotor dengesizliği (ani, doğrusal, basamak, dirac, üstel)
│       ├── 10.csv - 11.csv        # Döngüdeki su miktarında yavaş/ani artış
│       ├── 12.csv                 # Kavitasyona kadar tanktan su tahliyesi
│       ├── 13.csv                 # Pompa girişine iki fazlı akış verilmesi (kavitasyon)
│       └── 14.csv                 # Yüksek sıcaklıkta su beslemesi
├── docs/                          # Görseller ve mimari dokümantasyonu
└── notebooks/                     # Algoritma karşılaştırma defterleri
```
Toplam **35 adet CSV dosyası** mevcuttur. Ayrıştırma hatası bulunmamaktadır. Tüm dosyalarda sütun ayırıcısı noktalı virgül (`;`) olarak doğrulanmıştır.

---

## 2. Dosya Envanteri ve Zaman Sürekliliği Analizi

Tüm 35 CSV dosyasının satır satır analizi yapılarak `results/data_review/inventory.csv` dosyasına işlenmiştir. Öne çıkan bulgular şunlardır:

1. **Satır Sayısı:**
   - Toplam satır sayısı: 46.804
   - `anomaly-free.csv`: 9.405 satır (en uzun dosya)
   - 34 anomali deney dosyası: 745 ile 1.155 satır arasında (ortalama ~1.100 satır)
2. **Eksik Değerler (Missing Values):**
   - Ham CSV dosyalarında hiçbir hücrede `NaN`, `null` veya boş değer **bulunmamaktadır** (Eksik değer sayısı = 0).
3. **Zaman Damgaları (datetime):**
   - Geçersiz veya okunamayan zaman damgası: 0
   - Tekrarlanan (duplicate) zaman damgası: 0
   - Zaman serisi sırası: Tüm dosyalarda kesin monoton artandır (`is_monotonic = True`).
4. **Örnekleme Sıklığı ve Zaman Boşlukları (Time Gaps):**
   - Nominal örnekleme periyodu: **1 saniye (1 Hz)** (medyan dt = 1.00 sn).
   - Ancak zaman serisinin kesintisiz olduğu varsayımı **tüm dosyalarda geçerli değildir**. 7 deney dosyasında belirgin zaman atlamaları (veri kaybı/gecikme) tespit edilmiştir:
     - `other/2.csv`: Maksimum dt = **247 saniye** (büyük kesinti)
     - `valve1/2.csv`: Maksimum dt = **76 saniye**
     - `valve1/7.csv`: Maksimum dt = **65 saniye**
     - `valve2/1.csv`: Maksimum dt = **64 saniye**
     - `valve1/4.csv`: Maksimum dt = **54 saniye**
     - `other/13.csv`: Maksimum dt = **33 saniye**
     - `other/12.csv`: Maksimum dt = **5 saniye**

> **Gözlem:** Dosyalar harici zaman serisi modellerine verilirken veya pencereleme (windowing) yapılırken bu zaman atlamaları göz ardı edilmemeli; 1 Hz sabit aralık varsayımı körü körüne uygulanmamalıdır.

---

## 3. Veri Sözlüğü ve Kolon Kalite İncelemesi

Kolon bazlı istatistikler ve veri bütünlüğü `results/data_review/column_quality.csv` dosyasına çıkarılmıştır.

| Kolon Adı | Veri Tipi | README'deki Birim | Fiziksel Açıklama | Tipik Değer Aralığı (Min - Max) | Kalite ve Davranış Notu |
| :--- | :---: | :---: | :--- | :---: | :--- |
| `datetime` | String (ISO) | - | Ölçümün veritabanına kayıt anı (YYYY-MM-DD hh:mm:ss) | 2020-02-08 ... 2020-03-01 | Monoton artan, 1 Hz nominal. |
| `Accelerometer1RMS` | Float64 | g | 1 Nolu İvmeölçer RMS titreşim ivmesi | 0.019 g - 1.485 g | Rotor balanssızlığında dramatik artış gösterir. |
| `Accelerometer2RMS` | Float64 | g | 2 Nolu İvmeölçer RMS titreşim ivmesi | 0.038 g - 1.776 g | 1 Nolu sensörle yüksek korelasyonludur. |
| `Current` | Float64 | A | Motor elektrik akımı | 0.40 A - 3.25 A | Vana kapanmalarında ve yük değişimlerinde dalgalanır. |
| `Pressure` | Float64 | Bar | Pompa çıkışındaki kapalı devre hidrolik basıncı | -0.273 bar - 0.722 bar | Negatif değerler bağıl (gauge) vakum seviyesidir; sensör hatası değildir. |
| `Temperature` | Float64 | °C | Elektrik motoru gövde sıcaklığı | 40.2 °C - 98.4 °C | Yavaş değişen termal atalet gösterir; anlık değişim içermez. |
| `Thermocouple` | Float64 | °C | Sirkülasyon devresindeki akışkan (su) sıcaklığı | 19.8 °C - 38.6 °C | Yavaş eğilim sergiler; su ekleme/tahliyeden etkilenir. |
| `Voltage` | Float64 | V | Motor şebeke gerilimi | 200.1 V - 243.5 V | Sürekli gürültülü dalgalanma (şebeke salınımı) gösterir. |
| `Volume Flow RateRMS` | Float64 | L/min | Döngü içindeki hacimsel akış debisi RMS | 0.0 L/dk - 132.8 L/dk | Vana kapatma ve kavitasyon deneylerinde doğrudan etkilenir. README'de `RateRMS` olarak kısaltılmıştır. |
| `anomaly` | Float64 | {0.0, 1.0} | Noktasal/Aralıksal anomali etiketi | 0 veya 1 | Sadece 34 deney dosyasında vardır. `anomaly-free.csv`'de yoktur! |
| `changepoint` | Float64 | {0.0, 1.0} | Değişim noktası göstergesi | 0 veya 1 | Anomali geçişlerinde (başlangıç, kademe, bitiş) 1 olur (deney başına 2-4 adet). |

---

## 4. Keşifsel Veri İncelemesi: Seçilen Deneyler ve Görselleştirme

Temsili davranışları incelemek üzere 3 farklı fiziksel mekanizmayı temsil eden deneyler seçilmiş ve alt grafikler halinde `results/data_review/` altına kaydedilmiştir.

### 4.1. Deney 1: `valve1/1.csv` (Pompa Giriş Vanası Kapatma)
- **Görsel:** `results/data_review/experiment_valve1_1.png`
- **Seçim Gerekçesi:** Hidrolik süreç anomalisinin (akış kısıtlaması) sistem genelindeki çok değişkenli etkisini incelemek.
- **Bulgular ve Gözlemler:**
  - Toplam satır: 1.145. Anomali aralığı: 572 ile 973 indeksleri arası (402 saniye).
  - Değişim noktaları (`changepoint=1`): İndeks 572 (kapatma başlangıcı), 629 (tam kısılma), 916 (açılma başlangıcı), 974 (normale dönüş).
  - `Volume Flow RateRMS` debisi 32 L/dk seviyesinden anomali bölgesinde dalgalanarak düşmektedir.
  - Basınç ve akım sinyallerinde vana hareketine bağlı mikro salınımlar gözlenmektedir.
  - İvmeölçerler (`Accelerometer1RMS`, `Accelerometer2RMS`) ve sıcaklık sensörleri bu hidrolik müdahaleden neredeyse hiç etkilenmemiştir (ortalama ivme 0.027 g sabit kalmıştır).

### 4.2. Deney 2: `other/5.csv` (Rotor Mekanik Balanssızlığı - Ani Davranış)
- **Görsel:** `results/data_review/experiment_other_5.png`
- **Seçim Gerekçesi:** Mekanik titreşim arızalarının hidrolik parametrelerden bağımsız karakterini ve ani değişim davranışını incelemek.
- **Bulgular ve Gözlemler:**
  - Toplam satır: 1.155. Anomali aralığı: 572 ile 981 indeksleri arası (410 saniye).
  - Değişim noktaları: 572 (ani başlangıç) ve 982 (dönüş).
  - `Accelerometer1RMS`: Normalde ortalama **0.217 g** iken anomali başladığı anda **0.632 g** seviyesine (~3 kat) fırlamaktadır.
  - `Accelerometer2RMS`: Normalde **0.269 g** iken anomali anında **0.735 g** seviyesine çıkmaktadır.
  - Hidrolik debi (`Volume Flow RateRMS` ~126 L/dk), motor akımı (~2.44 A) ve sıcaklık değerleri mekanik dengesizlikten neredeyse hiç etkilenmemiştir.
  - **Kritik Karar Çıkarımı:** Bu deney, sensör bazlı anomali lokalizasyonu ve kanala özgü bozulma ayrımı için mükemmel bir zemin sunmaktadır.

### 4.3. Deney 3: `other/13.csv` (Pompa Girişinde İki Fazlı Akış / Kavitasyon)
- **Görsel:** `results/data_review/experiment_other_13.png`
- **Seçim Gerekçesi:** Akışkan dinamiğindeki faz değişiminin (hava/su karışımı) hem akış hem basınç üzerindeki karmaşık ve gürültülü etkisini incelemek.
- **Bulgular ve Gözlemler:**
  - Toplam satır: 923. Anomali aralığı: 495 ile 759 indeksleri arası (265 saniye).
  - Değişim noktaları: [495, 520, 746, 760].
  - Bu deneyde 33 saniyelik bir veri iletim atlaması (`dt_max = 33s`) bulunmaktadır.
  - Anomali sırasında debi (`Volume Flow RateRMS`) 98 L/dk'dan 114 L/dk'ya fırlamakta ve şiddetli türbülanslı dalgalanmalar sergilemektedir.
  - Akım sinyali 2.37 A'dan 2.43 A'ya yükselmekte, hidrolik dengesizlik motor yüküne yansımaktadır.

### 4.4. Referans İnceleme: `anomaly-free/anomaly-free.csv`
- **Görsel:** `results/data_review/experiment_anomaly_free.png`
- **Seçim Gerekçesi:** Müdahale edilmemiş kararlı durum referansı.
- **Bulgular:**
  - Dosyada `anomaly` ve `changepoint` kolonları mevcut değildir.
  - 9.405 saniye boyunca motor gövde sıcaklığı 90°C civarında doyuma ulaşmış, akış debisi ~122 L/dk seviyesinde stabil kalmıştır.

---

## 5. Veri Uygunluğu Kararı (Data Suitability Assessment)

Araştırma ve Tasarım Karar Metni (`pdf's/26.10.2026.pdf`) ve TÜBİTAK 2209-A Taslağı ışığında kanıta dayalı değerlendirme:

### 5.1. Veri Hangi Fiziksel Sistemi ve Koşulları Temsil Ediyor?
SKAB, laboratuvar ortamında kontrollü bir su devridaim test düzeneğini temsil etmektedir. Endüstriyel makinelerde yaygın görülen santrifüj pompa, elektrik motoru, boru hattı ve vanaları içerir. Gerçek fabrika ortamındaki ortam sıcaklığı dalgalanmaları ve çoklu makine gürültüsü bulunmamakla birlikte hidrolik ve mekanik etkileşimleri gerçeğe yakın yansıtır.

### 5.2. Etiketler Neyi Gösteriyor ve Nasıl Elde Edilmiş?
- SKAB etiketleri (`anomaly=1`), operatörün test düzeneğine fiziksel olarak uyguladığı müdahalenin (vanayı kısma, rotor dengesini bozma, kavitasyon oluşturma vb.) zaman aralığıdır.
- `changepoint=1`, bu müdahalelerin başlangıç, kademe ve bitiş anlarındaki dinamik rejim değişimlerini gösterir.
- **ÖNEMLİ KANIT SINIRI:** Etiketler **süreç müdahalesi etiketidir**. Veri setinde "bu bir sensör arızasıdır" veya "sensör sağlamdır" şeklinde ayrıştırılmış bir **sensör sağlık etiketi bulunmamaktadır**.

### 5.3. Sensör Arızası ile Süreç Anomalisi Ayrı Doğrulanabiliyor mu?
- **HAYIR.** SKAB verisi kendi başına fiziksel sensör arızası ile süreç anomalisini ayıramaz.
- **Çözüm:** TÜBİTAK 2209-A araştırma taslağında öngörüldüğü üzere; sensör/veri kalitesi ayrımı, veriye kontrollü sentetik bozulmalar (drift, stuck-at, packet loss/eksik veri, gürültü) eklenerek ve dörtlü değerlendirme matrisi kurularak test edilmelidir:
  1. *Normal Süreç + Sağlam Sensör* (Kaynak 0, Bozulma Yok)
  2. *Normal Süreç + Bozuk Sensör* (Kaynak 0, Sentetik Bozulma Var)
  3. *Anormal Süreç + Sağlam Sensör* (Kaynak 1, Bozulma Yok)
  4. *Anormal Süreç + Bozuk Sensör* (Kaynak 1, Sentetik Bozulma Var)

### 5.4. Desteklenen İddialar
1. Çok değişkenli endüstriyel sensör zaman serilerinde normal davranış ve süreç sapmalarının modellenmesi.
2. Sentetik olarak enjekte edilen sensör bozulmalarının (kayma, donma, eksik veri) anomali tespit modelleri üzerindeki yanlış alarm artırıcı etkisinin ölçülmesi.
3. Ayrı bir sensör doğrulama/kalite katmanının, sensör bozulması kaynaklı yanlış süreç alarmlarını filtreleme başarısının kanıtlanması.

### 5.5. Desteklenmeyen (Kaçınılması Gereken) İddialar
1. *"SKAB etiketleri gerçek fiziksel sensör arızalarını doğrulamıştır"* iddiası desteklenmez.
2. *"Sistemimiz fabrikadaki her türlü sensör ve süreç arızasını kesin ayırt etmektedir"* iddiası yapılamaz (Sentetik bozulma saha doğrulaması sayılmaz).
3. Etiket kolonu bulunmayan `anomaly-free.csv` dosyasına otomatik normal etiketi verip doğrudan test kümesi olarak genelleme yapılamaz; eğitim referansı olarak tutulmalıdır.

### 5.6. Açık Sorular ve Danışman Doğrulaması Gerektiren Noktalar
1. **Deney Bazlı Bölme:** 34 anomali dosyasından hangilerinin eğitim/doğrulama, hangilerinin nihai test kümesine ayrılacağı (ör. her arıza tipinden en az bir dosya teste mi ayrılmalı?).
2. **Sentetik Bozulma Şiddetleri:** Yavaş kayma (drift) ve eksik veri (paket kaybı) için belirlenecek başlangıç genlik ve süre parametreleri.
3. **Zaman Atlamaları:** 7 dosyada görülen 5s - 247s arasındaki veri boşluklarının enterpolasyonla mı doldurulacağı yoksa modelin bunu da bir veri kalitesi göstergesi olarak mı ele alacağı.

---

## 6. Bir Sonraki Aşama İçin Gerekçeli Öneriler

1. **Deney/Seri Bazlı Veri Bölme Planı (Öneri):**
   - Sızıntı olmaması için aynı dosya bölünerek eğitim ve test yapılmamalıdır.
   - `anomaly-free.csv`'nin ilk kısmı temel normal model eğitimi için,
   - `valve1`, `valve2` ve `other` altındaki dosyaların dengeli bir alt kümesi doğrulama ve eşik belirleme için,
   - Kalan bağımsız deney serileri ise nihai sentetik bozulma testleri için ayrılmalıdır.
2. **Kontrollü Bozulma Ortamı (Öneri):**
   - Ham veriyi bozmadan, sadece çalışma anında bellek üzerinde hedef kanala uygulanan kayma (drift) ve ardışık eksiklik (burst loss) enjektörü tasarlanmalıdır.
3. **Temel Karşılaştırma Modeli (Öneri):**
   - Karar Metni ve Taslak'ta belirtildiği üzere hafif, yorumlanabilir bir temel model (ör. Isolation Forest veya PCA tabanlı T²/Q istatistiği) ile başlanmalı; ardından ayrı sensör güvenilirlik skorlayıcısı eklenmelidir.
