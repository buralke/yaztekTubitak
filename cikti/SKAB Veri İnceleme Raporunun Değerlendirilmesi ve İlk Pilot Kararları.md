SKAB Veri İnceleme Raporunun Değerlendirilmesi ve İlk Pilot Kararları
Belge tarihi: 28 Ekim 2026
İncelenen belge: skab_veri_inceleme_ciktisi.md
Proje: Endüstriyel Sensör Verilerinde Sensör Sorunu ve Süreç Anomalisinin Ayrı Değerlendirilmesi
Belge durumu: İlk değerlendirme ve koşullu pilot planı

1. Genel Değerlendirme
İnceleme raporuna göre SKAB, ilk pilot çalışmamız için uygun bir başlangıç adayıdır. Ancak bu uygunluk koşulludur:

Zaman boşluklarının nasıl işleneceği belirlenmelidir.

Bazı fiziksel yorumların kaynak dayanakları eklenmelidir.

Eğitim, doğrulama ve test ayrımı kesinleştirilmelidir.

İlk pilotta kullanılacak dosyalar ve zaman aralıkları seçilmelidir.

1.1. İncelemenin sınırı
Bu değerlendirmede yalnızca veri inceleme raporu ele alınmıştır.

Raporda adı geçen aşağıdaki çıktılar henüz ayrıca incelenmemiştir:

Ham CSV dosyaları.

inventory.csv.

column_quality.csv.

Deney grafikleri.

Bu nedenle raporda yer alan sayısal bulgular, bağımsız olarak yeniden hesaplanmış sonuçlar değil, raporda bildirilen sonuçlar olarak kabul edilmektedir.

1.2. Temel araştırma kapsamı
Mevcut verinin desteklediği başlangıç araştırması dayanıklılık üzerine kurulmalıdır:

Mevcut anomali etiketleri altında, sentetik sensör bozulmalarına karşı tespit dayanıklılığını ve yanlış alarm davranışını incelemek.

Bu kapsam, gerçek fiziksel sensör arızalarını ve süreç arızalarını kesin biçimde ayırdığımız iddiasından daha sınırlıdır.

2. Veri Hangi Amaçlar İçin Uygun?
Raporda 35 CSV dosyası, sekiz sensör kanalı, kaynak anomali etiketleri ve ayrı deney grupları bulunduğu belirtilmektedir. Bağımsız sensör arızası etiketinin bulunmadığı da açıklanmaktadır.

Kullanım amacı	Mevcut değerlendirme
Veri okuma ve görselleştirme altyapısı	Uygun
Kontrollü kayma ve ölçüm kaybı üretmek	Uygun başlangıç adayı
Bozulmanın anomali tespitine etkisini ölçmek	Deney planı tamamlanırsa uygun
Gerçek sensör ve süreç arızalarını kesin ayırmayı kanıtlamak	Mevcut etiketler tek başına yeterli değil
Gerçek fabrika başarısı iddia etmek	Mevcut çalışma aşamasında uygun değil
Karar
Veriler topluca “uygun” veya “uygun değil” olarak sınıflandırılmayacaktır.

Her dosya için şu soru cevaplanacaktır:

Bu dosya hangi araştırma veya geliştirme amacı için uygundur?

3. Eksik Hücre ile Zaman Boşluğu Arasındaki Fark
Raporda toplam 46.804 satır incelendiği ve hiçbir hücrede eksik değer bulunmadığı belirtilmektedir. Bunun yanında yedi dosyada zaman atlamaları raporlanmıştır.

Bu iki bulgu birbiriyle çelişmez.

Hücrelerde eksik değer bulunmaması, zaman ekseninde ölçüm kaybı olmadığı anlamına gelmez.

Açıklama amaçlı örnek
text
12:00:00 → 10.2
12:00:01 → 10.3
12:04:08 → 10.4
Bu tabloda boş hücre bulunmamaktadır. Ancak iki kayıt arasında uzun bir zaman boşluğu vardır.

Karar
Veri kalite değerlendirmesinde iki ayrı kontrol tutulacaktır:

Kayıtlı satırlar içindeki eksik hücreler.

Zaman eksenindeki beklenmeyen aralıklar.

“Eksik hücre: 0” bulgusu, dosyaları kesintisiz zaman serileri olarak kabul etmek için tek başına yeterli değildir.

4. Zaman Boşlukları Bulunan Dosyaların Kullanımı
Raporda aşağıdaki zaman atlamaları bildirilmiştir:

Dosya	Bildirilen zaman atlaması
other/2.csv	247 saniye
valve1/2.csv	76 saniye
valve1/7.csv	65 saniye
valve2/1.csv	64 saniye
valve1/4.csv	54 saniye
other/13.csv	33 saniye
other/12.csv	5 saniye
4.1. İlk bozulma üreticisini geliştirmek için
İlk örnek olarak, zaman boşluğu bulunmadığı envanterden doğrulanan bir dosya tercih edilmelidir.

Amaç, yazılımla eklenen ölçüm kaybının etkisini, verinin önceden var olan zaman boşluklarından ayrı değerlendirebilmektir.

4.2. Sonraki dayanıklılık deneyleri için
Zaman boşluğu bulunan dosyalar otomatik olarak elenmemelidir.

Bu dosyalar, önceden var olan veri kesintileri altında sistemin davranışını değerlendirmek için ayrı bir deney grubu olarak kullanılabilir.

4.3. Başlangıç için önerilen boşluk politikası
Zaman boşluklarını kaydet.

Boşlukları aşan geçmiş pencerelerini işaretle.

Gerekli geçmiş veri bulunmuyorsa karar verilemediğini belirt.

Doldurma yöntemlerini daha sonra ayrı deney koşulları olarak karşılaştır.

Uzun boşlukları sessizce doldurma.

Bu politika henüz nihai yöntem değildir; ilk pilot için önerilen başlangıç yaklaşımıdır.

4.4. Raporda düzeltilmesi gereken neden açıklaması
Raporda boşluklar veri iletim gecikmesi veya kayıt kesintisiyle ilişkilendirilmiştir. Ancak yalnızca zaman damgaları, fiziksel nedeni kesinleştirmek için yeterli kabul edilmemelidir.

Önerilen ifade:

Zaman damgalarında beklenmeyen aralıklar gözlenmiştir. Bu aralıkların nedenleri mevcut incelemede doğrulanmamıştır.

5. Debi Kolonunun İsim Eşleştirmesi
Rapora göre README içinde RateRMS olarak geçen değişken, CSV dosyalarında Volume Flow RateRMS adıyla bulunmaktadır.

Bu farklılık veri setini eleme nedeni değildir. Ancak veri yükleme katmanında açık bir eşleştirme yapılmalıdır.

Önerilen eşleştirme
Kaynak kolon	Proje içi standart isim	Açıklama
Volume Flow RateRMS	flow_rate_rms	Kaynak belgedeki debi değişkeniyle eşleştirilen alan
Karar
Ham dosyadaki kolon adı korunacaktır.

Gerekirse proje içinde standart bir isim kullanılacaktır.

Kaynak kolon ile standart isim arasındaki eşleştirme veri sözlüğüne yazılacaktır.

Temel ilke:

Kolon adındaki farklılık tek başına kalite sorunu değildir; yanlış eşleştirme yapılması sorundur.

6. Negatif Basınç Değerlerinin Değerlendirilmesi
Raporda negatif basınçların bağıl basınç nedeniyle fiziksel olarak geçerli olduğu ve doğrulandığı belirtilmektedir. Ancak rapor içinde bu doğrulamanın açık kaynak bölümü, alıntısı veya referans ölçüm bilgisi gösterilmemektedir.

Bu nedenle aşağıdaki iki kesin karardan da kaçınılmalıdır:

Negatif değerlerin otomatik olarak hata kabul edilmesi.

Kaynak dayanağı görülmeden bütün negatif değerlerin kesin doğru kabul edilmesi.

Önerilen kayıt
Negatif basınç değerleri gözlenmiştir. Kullanılan basınç referansı ve sensör tanımı kaynak belge üzerinden doğrulanacaktır. Bu aşamada otomatik silme uygulanmayacaktır.

Karar
Negatif basınç değerleri yalnızca işaretleri nedeniyle silinmeyecektir. Fiziksel anlamları kaynak belgelerle ilişkilendirilecektir.

Diğer fiziksel yorumlar
Aynı yaklaşım şu deney adları için de uygulanacaktır:

Rotor balanssızlığı.

Kavitasyon.

İki fazlı akış.

Giriş veya çıkış vanası müdahalesi.

Her dosya ile fiziksel deney türü arasındaki eşleştirmenin kaynak dayanağı kayıt altına alınmalıdır. Raporda bu tür adlandırmalar kullanılmaktadır.

7. anomaly-free.csv Dosyasının Kullanımı
Rapora göre bu dosya:

9.405 satır içermektedir.

Sekiz sensör kanalı ve zaman bilgisine sahiptir.

anomaly ve changepoint kolonlarını içermemektedir.

Kaynak belgelerde normal çalışma referansı olarak tanımlanmaktadır.

Kullanım yaklaşımı
Yalnızca dosya adına bakılarak otomatik etiket üretilmeyecektir.

Normal referans tanımı kaynak belgeyle ilişkilendirilecektir.

Dosyanın eğitim veya değerlendirme rolü baştan belirlenecektir.

Aynı kayıtlar hem eğitimde kullanılıp hem bağımsız test örnekleri olarak sunulmayacaktır.

Rapordaki veri sızıntısı ifadesine düzeltme
Kaynağın normal referans olarak tanımladığı bir dosyaya bu bilgiyi kaydetmek, tek başına veri sızıntısı anlamına gelmez.

Birbirinden ayrılması gereken konular şunlardır:

Dosyanın kaynakta nasıl tanımlandığı.

Dosyanın model geliştirme ve değerlendirme sürecinde nasıl kullanıldığı.

Asıl dikkat edilmesi gereken, geliştirme ve bağımsız değerlendirme rollerinin karışmamasıdır.

Öneri
İlk pilotta dosyanın tamamının eğitim referansı olarak ayrılması değerlendirilebilir. Bu seçim henüz nihai veri bölme kararı değildir.

8. Dört Deney Koşulunun Doğru Adlandırılması
Raporda “sağlam sensör” ve “bozuk sensör” ifadeleri kullanılmıştır. Aynı raporda gerçek sensör sağlığı etiketi bulunmadığı da belirtilmektedir.

Bu nedenle deney koşulları aşağıdaki gibi adlandırılmalıdır:

Kaynak anomali etiketi	Sentetik bozulma	Kullanılacak ifade
0	Yok	Normal etiketli, ek bozulma uygulanmamış
0	Var	Normal etiketli, sentetik bozulma uygulanmış
1	Yok	Anomali etiketli, ek bozulma uygulanmamış
1	Var	Anomali etiketli, sentetik bozulma uygulanmış
Temel ilke
Ek bozulma uygulanmamış olması, fiziksel sensörün kesin sağlam olduğunu kanıtlamaz.

Bu terminoloji, çalışmanın değerini azaltmaz. Ölçülen durum ile fiziksel neden iddiasını birbirinden ayırır.

9. Eğitim, Doğrulama ve Test Ayrımı
Raporda önerilen genel yapı şöyledir:

Eğitim: Normal referans ve seçilen deneylerin normal bölgeleri.

Doğrulama: Farklı türlerden seçilmiş 6–8 deney.

Test: Kalan 20’den fazla deney.

Bu yapı henüz kesin dosya listesiyle tamamlanmış değildir.

9.1. Kapatılması gereken soru
Eğitim için normal bölümü kullanılan bir deneyin kalan kısmı hangi grupta kalacaktır?

9.2. İlk pilot için önerilen kural
Bir deneyin herhangi bir bölümü eğitim amacıyla kullanılıyorsa, o deneyin tamamı eğitim grubuna atanmalıdır.

Aynı deneyin kalan anomalili kısmı bağımsız doğrulama veya test verisi olarak kullanılmamalıdır.

Aynı deneyden üretilen bütün sentetik kopyalar da aynı veri bölümünde kalmalıdır.

9.3. Bölme kayıt biçimi
text
experiment_id,split,intended_use,reason
Örnek kayıt:

text
örnek_deney,train,normal_baseline,eğitim referansı
9.4. Rapordaki ifadenin netleştirilmesi
“Satır bazında bölmek sızıntıya neden olur” ifadesi yerine, bu araştırmanın kuralı şu şekilde yazılmalıdır:

Bu araştırmada aynı deneyin ilişkili zaman noktalarının eğitim ve bağımsız test arasında karışmasını önlemek için deney bazlı ayrım uygulanacaktır.

Karar
Kesin dosya dağılımı yalnızca sayısal oranlara göre yapılmayacaktır. Deney türleri, kullanım amaçları ve veri uygunluğu birlikte değerlendirilecektir.

10. İlk Pilot İçin Dosya Adayları
Raporda aşağıdaki deneylerin grafiklerinin üretildiği belirtilmektedir:

valve1/1.csv

other/5.csv

other/13.csv

other/13.csv için ayrıca 33 saniyelik zaman atlaması bildirilmiştir.

10.1. Öncelikli adaylar
İlk olarak şu iki dosyanın incelenmesi önerilmektedir:

valve1/1.csv

other/5.csv

Bu dosyalar için grafik hazırlanmış olması ve zaman boşluğu listesinde adlarının yer almaması, onları başlangıç adayı yapmaktadır. Ancak kesin seçim için envanter ve grafik kontrolü gereklidir.

Seçim koşulları
Zaman yapısı doğrulanmış olmalıdır.

Kaynak etiketleri anlaşılmış olmalıdır.

Normal ve anomali etiketli aralıkların uzunlukları bilinmelidir.

Bozulma eklemek için yeterli zaman aralığı bulunmalıdır.

Açıklanmamış başlangıç veri kalitesi sorunları belirlenmelidir.

10.2. Sonraki dayanıklılık adayı
other/13.csv, önceden var olan zaman boşluklarını da içeren dayanıklılık değerlendirmesi için saklanabilir.

Bu yaklaşım, ilk yazılım denemesini sade tutarken daha zor durumların değerlendirme dışında bırakılmasını önler.

11. Mevcut Karar Tablosu
Başlık	Mevcut durum	Sonraki işlem
Dosyaların okunabilirliği	Rapora göre olumlu	Envanterle kontrol
Ham hücrelerde eksiklik	Rapora göre yok	Kolon kalite özetiyle kontrol
Zaman düzeni	Yedi dosyada boşluk bildirilmiş	Boşluk politikası belirle
Sensör kolon şeması	İsim eşleştirmesi gerekiyor	Veri sözlüğü oluştur
Gerçek sensör arızası etiketi	Bulunmadığı bildiriliyor	İddiaları sentetik bozulma kapsamına sınırla
Fiziksel yorumlar	Bazıları kaynak dayanağı gerektiriyor	Belge referanslarını ekle
Veri bölme	Öneri var, kesin liste yok	Deney kimlikleriyle sabitle
İlk pilot dosyaları	Adaylar var	Grafik ve aralık uzunluklarıyla seç
Genel karar
Bu aşamada dosyalar topluca elenmeyecektir. Kullanım amaçlarına göre gruplandırılacaktır.

12. Dosya Bazında Kullanılacak Değerlendirme Formu
text
Dosya / deney kimliği:

1. Kaynak ve sürüm belli mi?
Cevap:

2. Sensör kolonları ve anlamları belli mi?
Cevap:

3. Zaman yapısında sorun var mı?
Cevap:

4. Kaynak etiketleri neyi temsil ediyor?
Cevap:

5. Etiketlerde eksik veya belirsiz durum var mı?
Cevap:

6. Başlangıç verisinde açıklanmamış bozulma var mı?
Cevap:

7. Normal ve anomali etiketli aralıkların uzunlukları yeterli mi?
Cevap:

8. Kayma senaryosu kurulabilir mi?
Cevap:

9. Ardışık ölçüm kaybı senaryosu kurulabilir mi?
Cevap:

10. Dosya hangi veri bölümüne atanacak?
Cevap:

11. Bu veriyle hangi iddia test edilebilir?
Cevap:

12. Bu veriyle hangi iddia test edilemez?
Cevap:

Karar:
- İlk pilot için uygun
- Koşullu uygun
- Belirli amaç için uygun
- İnceleme bekliyor
- Mevcut amaç için uygun değil

Kararın gerekçesi:

Çözülmesi gereken konular:

Karar tarihi:
13. Sonraki İnceleme İçin Gerekli Çıktılar
İlk deney seçimini kesinleştirmek için aşağıdaki çıktılar incelenmelidir:

inventory.csv

column_quality.csv

experiment_valve1_1.png

experiment_other_5.png

Bu çıktılar üzerinden şu kararlar verilecektir:

İlk pilotta hangi deney kullanılacak?

Hangi sensöre bozulma uygulanacak?

Hangi zaman aralığı seçilecek?

Kayma hangi büyüklükte ve sürede uygulanacak?

Ölçüm kaybı hangi aralıkta oluşturulacak?

Kaynak etiketleri ile sentetik müdahale kayıtları nasıl saklanacak?

14. Sonraki İşlerin Kontrol Listesi
Dosya envanterindeki sayısal bulguları kontrol et.

Kolon kalite özetini incele.

Zaman boşluklarını dosya ve konum bazında kaydet.

Negatif basınç yorumunun kaynak dayanağını ekle.

Fiziksel deney adlarının kaynak eşleştirmelerini doğrula.

Debi kolonu için standart isim eşleştirmesi oluştur.

Dört deney koşulunun terminolojisini düzelt.

anomaly-free.csv dosyasının kullanım rolünü belirle.

Deney bazlı eğitim, doğrulama ve test listelerini oluştur.

İlk pilot dosyasını seç.

İlk pilot sensörünü ve zaman aralığını belirle.

Bozulma üreticisinin parametrelerini kaydet.

Ham verinin değiştirilmediğini doğrula.

15. Sonuç ve Çalışma Sınırı
Mevcut rapor, SKAB üzerinde araştırmaya başlamanın mümkün olduğunu göstermektedir. Bununla birlikte ilk pilotun kesin dosya seçimi ve deney düzeni, raporda listelenen yardımcı çıktılar kontrol edildikten sonra tamamlanmalıdır.

Bu aşamada öncelik yeni veri setleri toplamaya devam etmek değil:

Mevcut bulguları kontrol etmek.

Belirsiz fiziksel yorumları belgelendirmek.

Veri bölme planını sabitlemek.

İlk kontrollü deneyin dosyasını, sensörünü ve zaman aralığını seçmektir.

Çalışmanın başlangıç iddiası şu kapsamda korunacaktır:

Mevcut anomali etiketleri altında, sentetik sensör bozulmalarının anomali tespitine etkisini ve ayrı veri kalitesi değerlendirmesinin sağlayabileceği katkıyı ölçmek.

