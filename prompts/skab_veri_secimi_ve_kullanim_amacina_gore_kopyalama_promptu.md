# Görev: SKAB Dosyalarını Kullanım Amaçlarına Göre Ayır ve Kopyala

## Amaç

Çalışma alanındaki SKAB veri inceleme raporunu ve bu raporun değerlendirmesini içeren Markdown dosyasını oku.

Bu belgelerdeki kararları esas alarak SKAB dosyalarını kullanım amaçlarına göre yeni bir klasör altında düzenle.

Bu aşamanın amacı model eğitmek veya kesin eğitim/doğrulama/test ayrımı yapmak değildir. Amaç, ilk pilot adaylarını, normal referansı, zaman boşluğu içeren deneyleri ve diğer değerlendirme adaylarını izlenebilir biçimde ayırmaktır.

## 1. Önce Kaynakları Bul ve Kontrol Et

Çalışma alanında aşağıdakileri bul:

- SKAB ham veri dizini.
- `skab_veri_inceleme_ciktisi.md`.
- SKAB inceleme raporunun değerlendirmesini ve pilot kararlarını içeren Markdown dosyası.
- `inventory.csv`.
- `column_quality.csv`.
- Kaynak README ve lisans dosyaları.
- Varsa örnek deney grafikleri.

Dosya konumlarını tahmin ederek işlem yapma. Önce gerçek yolları belirle.

Birden fazla SKAB kopyası varsa hangi kopyanın kaynak alınacağını belirle. Belirsizliği çözemiyorsan dosyaları kopyalamadan önce bana sor.

Envanter bulunmuyorsa ham CSV dosyalarını salt okunur biçimde inceleyerek gerekli kontrolleri yap. Doğrulayamadığın bulguları açıkça belirt.

## 2. Değişmez Kurallar

- Ham dosyaları taşıma, silme veya değiştirme.
- Yalnızca kopyalama yap.
- CSV içeriklerini, kolon adlarını ve kaynak etiketlerini değiştirme.
- Eksik değer doldurma, yeniden örnekleme veya aykırı değer temizleme yapma.
- Sentetik bozulma üretme.
- Model eğitme.
- Kesin eğitim/doğrulama/test ayrımı yapma.
- “Ek bozulma uygulanmamış” durumunu “sensör kesin sağlam” şeklinde adlandırma.
- Bir dosyanın etiket kolonları bulunmadığı için otomatik normal etiketi üretme.
- Kaynakta bulunmayan dosyaları oluşturulmuş veya kopyalanmış gibi gösterme.
- Önceden var olan farklı içerikteki dosyaların üzerine yazma.

## 3. Hedef Klasörü Oluştur

Proje kökünde aşağıdaki yapıyı oluştur:

SKAB_kullanim_plani/
├── README.md
├── manifest.csv
├── copy_verification.csv
├── 00_belgeler/
├── 01_pilot_adaylari/
├── 02_normal_referans_adayi/
├── 03_zaman_boslugu_degerlendirmesi/
├── 04_diger_deney_adaylari/
├── 05_inceleme_bekleyenler/
└── 06_grafikler_ve_raporlar/

Mevcut proje içinde aynı isimli hedef klasör varsa önce içeriğini kontrol et.

- Aynı içerikli dosyalar varsa yeniden kopyalamayı atla ve kaydet.
- Aynı hedef yolunda farklı içerik varsa üzerine yazma; çakışmayı bildir.
- Kaynak klasörü hedef klasör olarak seçme.
- Hedef klasörü kaynak taramasına dahil ederek tekrar tekrar kopyalama yapma.

## 4. Dosyaları Şu Amaçlarla Ayır

### 4.1. İlk Pilot Adayları

Öncelikle şu dosyaları kontrol et:

- `valve1/1.csv`
- `other/5.csv`

Bu dosyaları yalnızca aşağıdaki başlangıç kontrolleri uygunsa
`01_pilot_adaylari/` altına kopyala:

- Dosya okunabiliyor.
- Beklenen sensör ve etiket kolonları bulunuyor.
- Zaman damgaları geçerli ve sıralı.
- Tekrarlanan zaman damgaları yok veya açıklanmış.
- Envanterde belirtilen zaman yapısıyla çelişki yok.
- Normal ve anomali etiketli örneklerin sayıları kayıt altına alınabiliyor.

Dosyaları kaynak alt klasörlerini koruyarak yerleştir:

01_pilot_adaylari/
├── valve1/
│   └── 1.csv
└── other/
    └── 5.csv

Kullanım amacı:

> Veri yükleme, görselleştirme ve ileride geliştirilecek kontrollü kayma/ölçüm kaybı üreticisinin ilk denemeleri için aday deneyler.

Bu klasöre alınmaları, nihai eğitim veya test grubuna atandıkları anlamına gelmez.

Kontrollerde açıklanmamış sorun bulunursa dosyayı
`05_inceleme_bekleyenler/` altına kopyala ve gerekçesini yaz.

Bu iki dosyanın yerine başka pilot dosyası seçimini kendiliğinden kesinleştirme. Gerekirse alternatif öner.

### 4.2. Normal Referans Adayı

Şu dosyayı kontrol et:

- `anomaly-free/anomaly-free.csv`

Bulunursa `02_normal_referans_adayi/anomaly-free/` altına kopyala.

Kullanım amacı:

> Kaynak belgelerdeki normal referans tanımı doğrulandıktan sonra, normal davranış incelemesi ve olası temel model eğitimi için değerlendirilecek dosya.

Kurallar:

- Etiket kolonu ekleme.
- “Kesin eğitim verisi” olarak işaretleme.
- Kaynak belgenin normal referans tanımını doğrulayamadıysan bunu manifestte açıkça belirt.
- Bu dosyanın ilerideki eğitim/test rolünü henüz kesinleştirme.

### 4.3. Zaman Boşluğu Değerlendirmesi

Raporda aşağıdaki dosyalarda zaman boşlukları bildirilmiştir:

- `other/2.csv`
- `valve1/2.csv`
- `valve1/7.csv`
- `valve2/1.csv`
- `valve1/4.csv`
- `other/13.csv`
- `other/12.csv`

Bu listeyi yalnızca önceki rapora dayanarak körlemesine uygulama.

Envanter ve gerektiğinde ham zaman damgaları üzerinden:

- Zaman boşluğunun varlığını,
- En büyük ardışık zaman farkını,
- Kullanılan boşluk tespit ölçütünü

kontrol et.

Doğrulanan dosyaları kaynak alt klasörlerini koruyarak
`03_zaman_boslugu_degerlendirmesi/` altına kopyala.

Kullanım amacı:

> Önceden var olan zaman kesintileri altında veri kalitesi ve anomali tespit davranışının ileride ayrı değerlendirilmesi.

Kurallar:

- Bu dosyaları “kullanılamaz” olarak etiketleme.
- Boşlukları doldurma.
- Zaman farkını doğrudan kayıp örnek sayısı olarak yazma.
- Boşlukların nedenini kanıt olmadan iletişim arızası veya kayıt arızası diye kesinleştirme.

Raporda belirtilen dosya ile ölçüm sonucu çelişiyorsa dosyayı
`05_inceleme_bekleyenler/` altında tut ve çelişkiyi açıkla.

Listede olmayan başka dosyalarda da aynı ölçüte göre zaman boşluğu bulunursa bunları ayrıca kaydet ve uygun klasöre ayır.

### 4.4. Diğer Deney Adayları

Yukarıdaki gruplara girmeyen ve temel kontrolleri geçen CSV dosyalarını
`04_diger_deney_adaylari/` altına kopyala.

Kullanım amacı:

> Daha sonra deney bazında eğitim, doğrulama veya test rolü belirlenebilecek ek deney havuzu.

Bu klasördeki dosyaları otomatik olarak “test verisi” sayma.

### 4.5. İnceleme Bekleyenler

Şu durumlardan biri varsa dosyayı
`05_inceleme_bekleyenler/` altında tut:

- Okuma veya ayrıştırma hatası.
- Beklenmeyen kolon şeması.
- Açıklanmamış geçersiz zaman damgası.
- Kaynak rapor ve mevcut veri arasında çelişki.
- Etiket anlamının belirsizliği.
- Hangi kullanım grubuna ait olduğunun doğrulanamaması.

Her dosya için inceleme gerekçesini kaydet.

### 4.6. Belgeler, Raporlar ve Grafikler

Bulunan kaynak README ve lisans dosyalarını, kaynak yollarını koruyacak
şekilde `00_belgeler/` altına kopyala.

İnceleme raporları, envanter, kolon kalite özeti ve mevcut grafikleri
`06_grafikler_ve_raporlar/` altında düzenle.

Var olmayan grafik veya raporları mevcutmuş gibi listeleme.

## 5. Sınıflandırma Önceliği

Her kaynak CSV dosyasını yalnızca bir ana kullanım grubuna kopyala.

Karar sırası:

1. Açıklanmamış sorun veya çelişki varsa: inceleme bekleyenler.
2. Normal referans dosyasıysa: normal referans adayı.
3. Zaman boşluğu doğrulanmışsa: zaman boşluğu değerlendirmesi.
4. Belirtilen pilot adayıysa ve kontrolleri geçiyorsa: pilot adayları.
5. Diğer kontrolleri geçen deneyse: diğer deney adayları.

Bir dosyanın birden fazla potansiyel kullanım amacı varsa bunları manifestte ek kullanım notu olarak yaz. Gereksiz kopyalar üretme.

## 6. Manifest Oluştur

`manifest.csv` dosyasında her kaynak CSV için bir satır oluştur.

Alanlar:

- source_relative_path
- destination_relative_path
- usage_group
- intended_use
- assignment_status
- reason
- rows
- sensor_columns
- has_anomaly_label
- has_changepoint_label
- normal_label_count
- anomaly_label_count
- missing_cells
- invalid_datetime_count
- duplicate_timestamp_count
- time_sorted
- median_interval_seconds
- max_interval_seconds
- gap_detection_rule
- gap_count
- source_sha256
- destination_sha256
- copy_status
- notes

Hesaplayamadığın alanları uydurma. Boş bırak ve nedenini not et.

`assignment_status` için şu tür ifadeler kullan:

- provisional_pilot_candidate
- reference_candidate
- gap_evaluation_candidate
- unassigned_experiment_candidate
- needs_review

Nihai veri bölümü henüz seçilmediğinden `train`, `validation` veya `test`
ataması yapma.

## 7. Kopyalama Bütünlüğünü Doğrula

Kopyalanan her dosya için kaynak ve hedef SHA-256 özetlerini karşılaştır.

`copy_verification.csv` dosyasına şunları yaz:

- Kaynak yol.
- Hedef yol.
- Kaynak boyutu.
- Hedef boyutu.
- Kaynak SHA-256.
- Hedef SHA-256.
- Eşleşme sonucu.
- Hata veya çakışma notu.

Eşleşmeyen dosyaları başarılı olarak raporlama.

## 8. README Yaz

Hedef klasörün `README.md` dosyasında şunları açıkla:

1. Bu klasör neden oluşturuldu?
2. Her alt klasörde hangi dosyalar hangi amaçla tutuluyor?
3. Seçimler hangi belgelere ve kontrollere dayanıyor?
4. Hangi dosyalar inceleme bekliyor?
5. Ham verilerin değiştirilmediği.
6. Henüz eğitim/doğrulama/test ayrımı yapılmadığı.
7. Gerçek sensör sağlığının bu sınıflandırmayla kanıtlanmadığı.
8. Sentetik bozulma veya model eğitimi yapılmadığı.
9. Bir sonraki kararın pilot dosyası, sensör ve zaman aralığı seçimi olduğu.

Kullandığın boşluk tespit ölçütünü ve varsa kaynak sürümünü de kaydet.

## 9. İşlem Sonunda Bana Sun

Kısa bir sonuç raporu ver:

- Kullanılan kaynak ve hedef dizin.
- İncelenen toplam CSV sayısı.
- Her kullanım grubundaki dosya sayısı.
- Pilot adayları ve seçilme gerekçeleri.
- İnceleme bekleyen dosyalar ve nedenleri.
- Önceki rapordan farklı çıkan bulgular.
- Kopyalama bütünlüğü kontrolünün sonucu.
- Üretilen manifest, doğrulama ve README dosyaları.
- Benden beklenen sonraki kararlar.

Gerçekleştirmediğin işlemleri yapılmış gibi anlatma.

## Başlangıç Talimatı

Önce belgeleri ve dosyaları incele, ardından yukarıdaki kurallara göre
kopyalama ve kayıt işlemlerini gerçekleştir.

Kaynak dizin belirsizse veya farklı içerikli hedef dosyalarla çakışma varsa
ilgili işlemi durdur ve bana bildir.

Kopyalama tamamlandıktan sonra model eğitimine, veri temizlemeye veya
sentetik bozulma üretimine kendiliğinden geçme.