# SKAB İlk Veri İnceleme ve Değerlendirme Raporu

**Rapor Tarihi:** 28 Ekim 2026  
**Proje:** Endüstriyel Sensör Verilerinde Sensör Sorunu ve Süreç Anomalisinin Ayrı Değerlendirilmesi (TÜBİTAK 2209-A)  
**Hazırlayan:** Antigravity AI Araştırma Asistanı  

---

## 1. İncelemesi Yapılan Dosyalar ve Belgeler

* **Veri Kaynağı ve Belgeler:**
  * `SKAB/data/raw/SKAB/README.md` ve `SKAB/data/raw/SKAB/data/README.md` (Skoltech Anomaly Benchmark dokümantasyonu, sensör tanımları, deney açıklamaları).
  * `SKAB/data/raw/SKAB/LICENSE` (GPL-3.0 lisansı kontrol edildi).
  * `pdf's/26.10.2026.pdf` (*Endüstriyel Sensör Verilerinde Sensör Sorunu ve Süreç Anomalisinin Ayrı Değerlendirilmesi - Araştırma ve Yazılım Tasarımı Karar Metni*).
  * `pdf's/2209A_03_Endustriyel_Sensor_Detayli_Taslak_Makaleli-2.pdf` (TÜBİTAK 2209-A detaylı araştırma taslağı).
* **İncelenen Veri Dosyaları:**
  * `SKAB/data/raw/SKAB/data/` altındaki **35 adet CSV dosyasının tamamı**:
    * 1 adet normal referans dosyası: `anomaly-free/anomaly-free.csv`
    * 16 adet giriş vanası deneyi: `valve1/1.csv` ... `valve1/16.csv`
    * 4 adet çıkış vanası deneyi: `valve2/1.csv` ... `valve2/4.csv`
    * 14 adet diğer süreç müdahalesi deneyi: `other/1.csv` ... `other/14.csv`

---

## 2. Doğrulanan Bulgular

* **Dosya Biçimi ve Ayrıştırma:**
  * Tüm dosyalarda sütun ayırıcısının noktalı virgül (`;`) olduğu kesin olarak doğrulandı.
  * Ayrıştırma (parsing) hatası içeren veya okunamayan dosya bulunmamaktadır.
* **Veri Bütünlüğü ve Tipleri:**
  * 35 CSV dosyasının hiçbir hücresinde `NaN`, `null` veya boş kayıt **yoktur** (Eksik veri hücresi: 0).
  * Toplam **46.804 satır** ölçüm taranmıştır.
  * `anomaly-free.csv` 9.405 satırdan oluşurken, anomali deney dosyaları 745 ile 1.155 satır aralığındadır (ortalama ~1.100 satır).
* **Zaman Serisi Yapısı:**
  * `datetime` sütunu tüm dosyalarda `YYYY-MM-DD hh:mm:ss` formatında yer almaktadır.
  * Tekrarlanan (duplicate) veya geçersiz zaman damgası 0'dır.
  * Zaman sırası tüm dosyalarda kesin monoton artandır (`is_monotonic = True`).
  * Nominal örnekleme sıklığı **1 Hz (1 saniyede 1 ölçüm)** olarak teyit edilmiştir (medyan dt = 1.0 sn).
* **Sensörler ve Kolon Şeması:**
  * 34 anomali dosyasında standart 11 sütun mevcuttur:  
    `datetime`, `Accelerometer1RMS`, `Accelerometer2RMS`, `Current`, `Pressure`, `Temperature`, `Thermocouple`, `Voltage`, `Volume Flow RateRMS`, `anomaly`, `changepoint`.
  * `anomaly-free.csv` dosyasında ise etiket kolonları (`anomaly` ve `changepoint`) **bulunmamaktadır**; yalnızca 8 sensör ve `datetime` mevcuttur (9 sütun).
  * Kaynak README'de `RateRMS` olarak adlandırılan debi değişkeninin CSV dosyalarında `Volume Flow RateRMS` olarak yer aldığı saptanmıştır.
  * `Pressure` (basınç) sensöründeki negatif değerlerin (örn. -0.27 bar) hata değil, atmosferik basınca göre bağıl (gauge) vakum seviyesi olduğu fiziksel olarak doğrulanmıştır.

---

## 3. Tespit Edilen Sorunlar ve Belirsizlikler

1. **Zaman Atlamaları (Time Gaps):**
   * Ölçümlerin sürekli 1 saniye aralıkla aktığı varsayımı **tüm dosyalarda geçerli değildir**. 7 deney dosyasında veri iletim gecikmesi veya kayıt kesintisi kaynaklı boşluklar saptanmıştır:
     * `other/2.csv`: **247 saniye** atlama
     * `valve1/2.csv`: **76 saniye** atlama
     * `valve1/7.csv`: **65 saniye** atlama
     * `valve2/1.csv`: **64 saniye** atlama
     * `valve1/4.csv`: **54 saniye** atlama
     * `other/13.csv`: **33 saniye** atlama
     * `other/12.csv`: **5 saniye** atlama
2. **Etiket Derinliği ve Fiziksel Sınır:**
   * SKAB'daki `anomaly=1` etiketleri, operatörün test standına uyguladığı **süreç müdahalelerini** (vanayı kısma, rotor balanssızlığı, kavitasyon vb.) temsil etmektedir.
   * Veri setinde **bağımsız bir sensör arızası veya sensör sağlığı etiketi bulunmamaktadır**. Dolayısıyla ham SKAB verisi tek başına "bu anomali bir sensör bozulması mıdır yoksa süreç arızası mıdır?" ayrımını fiziki olarak kanıtlayamaz.
3. **`anomaly-free.csv` Etiket Durumu:**
   * Dosyada etiket sütunu yoktur. Kaynak belgeler bunun normal çalışma rejimi olduğunu belirtse de, teste doğrudan "normal etiketli" varsayımıyla eklenmesi metodolojik sızıntıya yol açabilir; öncelikle temel davranış öğreniminde eğitim referansı olarak korunmalıdır.

---

## 4. Projemiz Açısından Sonuç

* **Desteklenen İddialar ve Uygunluk:**
  * SKAB, santrifüj pompa, motor, vana ve boru döngüsünden oluşan çok değişkenli dinamik yapısıyla endüstriyel hidrolik/mekanik süreçleri temsil etmek için elverişlidir.
  * Kontrollü test ortamımızda, ham veriye yazılımsal sentetik bozulmalar (kayma, donma, ardışık veri kaybı) eklenerek **"mevcut süreç anomalisi etiketleri altında sentetik sensör bozulmalarına dayanıklılık ve yanlış alarm azaltma"** hipotezi ölçülebilir biçimde test edilebilir.
* **Kaçınılması Gereken İddialar:**
  * Projede *"fiziksel sensör arızalarını gerçek sahada kesin ayırt eden sistem"* iddiası kurulmamalıdır.
  * Sonuçlar Karar Metni'nde benimsenen **"Sentetik müdahaleler altındaki 4 değerlendirme durumu matrisi"** üzerinden raporlanmalıdır:
    1. Normal süreç + Sağlam sensör (Kaynak 0, Bozulma Yok)
    2. Normal süreç + Bozuk sensör (Kaynak 0, Sentetik Bozulma Var)
    3. Anormal süreç + Sağlam sensör (Kaynak 1, Bozulma Yok)
    4. Anormal süreç + Bozuk sensör (Kaynak 1, Sentetik Bozulma Var)

---

## 5. Üretilen Çıktılar ve Konumları

1. **Dosya Envanteri:**
   * `results/data_review/inventory.csv` — 35 dosyanın satır/kolon sayıları, zaman aralıkları, zaman atlamaları, etiket sayıları ve eksik değer dökümü.
2. **Kolon Kalite Özeti:**
   * `results/data_review/column_quality.csv` — 8 sensörün her bir dosyadaki min, max, ortalama, standart sapma ve ardışık sabit kalma (stuck-at) sayıları.
3. **Örnek Deney Zaman Serisi Grafikleri:**
   * `results/data_review/experiment_valve1_1.png` — *Giriş Vanası Kapatma*: Akış debisindeki düşüş ve basınç salınımları (8 alt grafik, kaynak anomali aralığı ve 4 değişim noktası işaretli).
   * `results/data_review/experiment_other_5.png` — *Rotor Balanssızlığı*: İvmeölçer titreşim genliğinin 0.22g'den 0.63g'ye (~3 kat) ani sıçraması.
   * `results/data_review/experiment_other_13.png` — *Kavitasyon / İki Fazlı Akış*: Akış debisindeki şiddetli türbülans ve 33 saniyelik zaman atlaması.
   * `results/data_review/experiment_anomaly_free.png` — Referans normal rejim profili.
4. **Detaylı Raporlar:**
   * `docs/dataset_review.md` — Kapsamlı veri uygunluk raporu.
   * `docs/decisions.md` — Terminoloji ve tasarım kararları kütüğü.

---

## 6. Beklenen Kararlar ve Önerilen Sonraki Adımlar

1. **Veri Bölme (Split) Stratejisi Kararı:**
   * *Öneri:* Aynı deney dosyasını satır bazında parçalamak sızıntıya neden olacağından, **dosya/deney bazlı ayrım** yapılması önerilir:
     * **Eğitim:** `anomaly-free.csv` (normal temel davranış) + `valve1`, `valve2`, `other` serilerinden seçilecek temsilci normal rejimler.
     * **Doğrulama (Validation / Eşik Ayarlama):** Farklı arıza tiplerinden seçilmiş 6-8 deney dosyası.
     * **Test:** Geriye kalan 20+ dosya (hiç görülmemiş seriler üzerinde kontrollü sentetik bozulma testleri).
2. **Zaman Atlamaları (Gaps) Kararı:**
   * 7 dosyada görülen zaman atlamaları (özellikle `other/2`'deki 247 saniye) enterpolasyonla mı doldurulmalı, yoksa model hattı bunu bir "iletişim/veri kaybı" olarak algılayıp doğrudan *Değerlendirilemiyor* veya veri kalitesi uyarısı mı üretmeli?
3. **İlk Sentetik Bozulma Pilotu:**
   * Ham veriye dokunmadan, zaman sıralı tekrar oynatma sırasında hedef sensöre (örn. `Volume Flow RateRMS` veya `Pressure`) **yavaş ölçüm kayması (drift)** ve **ardışık ölçüm kaybı (burst loss)** uygulayan test altyapısının kodlanması.