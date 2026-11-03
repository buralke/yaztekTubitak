# SKAB Veri Seti Kullanım Planı ve Organizasyon Dokümantasyonu

**Oluşturulma Tarihi:** 28 Ekim 2026  
**Kaynak Veri Seti:** Skoltech Anomaly Benchmark (SKAB v0.9, DOI: 10.34740/kaggle/dsv/1693952)  
**İlgili Proje:** Endüstriyel Sensör Verilerinde Sensör Sorunu ve Süreç Anomalisinin Ayrı Değerlendirilmesi (TÜBİTAK 2209-A)  
**Referans Belgeler:**  
- `pdf's/26.10.2026.pdf` (Araştırma ve Yazılım Tasarımı Karar Metni)  
- `pdf's/2209A_03_Endustriyel_Sensor_Detayli_Taslak_Makaleli-2.pdf` (TÜBİTAK 2209-A Taslak Metni)  
- `cikti/SKAB Veri İnceleme Raporunun Değerlendirilmesi ve İlk Pilot Kararları.md`  
- `cikti/skab_veri_inceleme_ciktisi.md`

---

## 1. Bu Klasör Neden Oluşturuldu?

Bu dizin yapısı, SKAB ham veri setindeki CSV dosyalarını, belgeleri ve ilk inceleme çıktılarını **kullanım amaçlarına göre izlenebilir, tekrarlanabilir ve kontrollü bir yapıda organize etmek** amacıyla oluşturulmuştur. 

Amaç, ham veriyi bozmadan veya kesin eğitim/doğrulama/test bölümlemesi yapmadan önce;
- İlk pilot adaylarını,
- Normal referans verisini,
- Zaman boşluğu (veri iletim/kayıt kesintisi) içeren deneyleri,
- Genel değerlendirme adaylarını
birbirinden şeffaf ve kanıta dayalı biçimde ayırmaktır.

---

## 2. Alt Klasörler ve Kullanım Amaçları

| Dizin Adı | Dosya Sayısı | Tanım ve Kullanım Amacı | Atama Statüsü |
| :--- | :---: | :--- | :--- |
| `00_belgeler/` | 3 | Kaynak SKAB README, data README ve GPL-3.0 lisans belgeleri. | `reference_document` |
| `01_pilot_adaylari/` | 2 | Veri yükleme, görselleştirme ve ileride geliştirilecek kontrollü kayma/ölçüm kaybı üreticisinin ilk denemeleri için aday deneyler (`valve1/1.csv`, `other/5.csv`). | `provisional_pilot_candidate` |
| `02_normal_referans_adayi/` | 1 | Kaynak belgelerdeki normal referans tanımı doğrultusunda, normal davranış incelemesi ve temel model eğitimi için değerlendirilecek referans dosya (`anomaly-free/anomaly-free.csv`). | `reference_candidate` |
| `03_zaman_boslugu_degerlendirmesi/` | 7 | Önceden var olan zaman kesintileri altında veri kalitesi ve anomali tespit davranışının ileride ayrı değerlendirilmesi için ayrılan deneyler. | `gap_evaluation_candidate` |
| `04_diger_deney_adaylari/` | 25 | Daha sonra deney bazında eğitim, doğrulama veya test rolü belirlenebilecek ek deney havuzu. | `unassigned_experiment_candidate` |
| `05_inceleme_bekleyenler/` | 0 | Açıklanmamış biçim, eksik veri veya etiket çelişkisi olan dosyalar için ayrılmıştır (Şu an tüm kontroller geçildiği için boştur). | `needs_review` |
| `06_grafikler_ve_raporlar/` | 10 | Veri envanteri, kolon kalite tablosu, inceleme raporları ve pilot deneylerin zaman serisi grafikleri. | `analysis_artifact` |

---

## 3. Seçimler Hangi Belgelere ve Kontrollere Dayanıyor?

Seçimler ve gruplamalar şu nesnel kontrollere dayandırılmıştır:
1. **Bağımsız Zaman Serisi Analizi:** 35 dosyanın tamamında `datetime` farkları ($dt$) incelenmiştir.
2. **Boşluk Tespit Ölçütü (Gap Detection Rule):**
   - SKAB nominal örnekleme periyodu **1.0 saniye (1 Hz)** olarak doğrulanmıştır (medyan dt = 1.0s).
   - Zaman adımı **$dt > 2.0$ saniye** olan durumlar zaman boşluğu (gap) olarak tanımlanmıştır.
   - Bu kurala göre tam 7 dosyada boşluk tespit edilmiştir:
     - `other/2.csv`: Maksimum dt = **247.0s** (1 adet boşluk)
     - `valve1/2.csv`: Maksimum dt = **76.0s** (1 adet boşluk)
     - `valve1/7.csv`: Maksimum dt = **65.0s** (1 adet boşluk)
     - `valve2/1.csv`: Maksimum dt = **64.0s** (1 adet boşluk)
     - `valve1/4.csv`: Maksimum dt = **54.0s** (1 adet boşluk)
     - `other/13.csv`: Maksimum dt = **33.0s** (31 adet boşluk)
     - `other/12.csv`: Maksimum dt = **5.0s** (34 adet boşluk)
   - Kalan 28 dosyanın hiçbirinde $dt > 2.0s$ aralığı bulunmamaktadır.
3. **Pilot Adaylarının Uygunluğu:**
   - `valve1/1.csv` (hidrolik vana müdahalesi) ve `other/5.csv` (mekanik rotor balanssızlığı) dosyalarında zaman boşluğu yoktur ($dt \le 2.0s$).
   - Her iki dosyada da anomali öncesi ~570 saniyelik temiz normal çalışma periyodu bulunmaktadır.
   - Kolon şemaları tamdır, eksik hücre 0'dır.
4. **Normal Referansın Uygunluğu:**
   - `anomaly-free.csv` kaynakta 9.405 saniyelik kesintisiz normal rejim olarak tanımlanmıştır. Etiket sütunu içermez.

---

## 4. Hangi Dosyalar İnceleme Bekliyor?

* `05_inceleme_bekleyenler/` klasöründe **şu an bekleyen dosya bulunmamaktadır**.
* Yapılan kontrollerde 35 dosyanın tamamı başarılı bir şekilde okunmuş, hiçbir dosyada `NaN` veya geçersiz zaman damgası görülmemiştir.
* İleride etiket tutarsızlığı veya fiziksel dayanak eksikliği tespit edilen dosyalar olursa bu klasöre taşınacaktır.

---

## 5. Değişmez Metodolojik İlkeler ve Garantiler

1. **Ham Verilerin Dokunulmazlığı:** Ham veri dosyaları (`SKAB/data/raw/SKAB/data/`) silinmemiş, taşınmamış veya içeriği değiştirilmemiştir. Yapılan işlem yalnızca salt okunur hash doğrulamalı kopyalamadır.
2. **Sentetik Bozulma ve Ön İşleme Yapılmamıştır:** Hiçbir dosyada eksik değer doldurma, aykırı değer temizleme, zaman serisi yeniden örnekleme (resampling) veya yapay bozulma üretilmemiştir.
3. **Eğitim / Doğrulama / Test Ayrımı Henüz Kesinleştirilmemiştir:** Bu klasörleme bir makine öğrenmesi veri bölmesi (train/val/test split) değildir. Hiçbir dosyaya nihai `train`, `val` veya `test` statüsü verilmemiştir (`assignment_status` alanları aday statüsündedir).
4. **Otomatik Etiket Üretilmemiştir:** Etiket sütunu bulunmayan `anomaly-free.csv` dosyasına otomatik `anomaly=0` sütunu eklenmemiştir.
5. **Gerçek Sensör Sağlığı İddiası Yoktur:** Ek bozulma uygulanmamış durumlar "sensör kesin sağlam" şeklinde yorumlanamaz. SKAB etiketleri süreç müdahalelerini temsil etmektedir.

---

## 6. Doğrulama ve Bütünlük

* Tüm dosyaların kopyalama bütünlüğü **SHA-256 kriptografik özetleri** ve **bayt boyutları** ile test edilmiştir.
* Kopyalanan 48 dosyanın (35 CSV, 3 belge, 10 rapor/grafik) 48'inde de **MATCH** sonucu alınmıştır.
* Ayrıntılı satır bazlı kayıtlar için:
  - [`manifest.csv`](manifest.csv): CSV dosyalarının metadata, kolon ve zaman istatistikleri dökümü.
  - [`copy_verification.csv`](copy_verification.csv): Kaynak/hedef dosya boyutu ve SHA-256 eşleşme tablosu.

---

## 7. Sonraki Adım ve Beklenen Kararlar

Bir sonraki aşamada kullanıcı/araştırmacı onayıyla:
1. `valve1/1.csv` ve `other/5.csv` adaylarından ilk pilot deney dosyasının seçilmesi,
2. Bozulma uygulanacak hedef sensör kanalının (örn. debi veya titreşim) belirlenmesi,
3. Müdahale zaman aralığı, kayma hızı ve ölçüm kaybı süresinin kararlaştırılması hedeflenmektedir.

