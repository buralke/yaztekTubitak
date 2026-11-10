# TÜBİTAK 2209-A Araştırma Önerisi Metinleri (Güncellenmiş ve Doğrulanmış Sürüm)

**Belge Tarihi:** 10 Kasım 2026  
**Referans Düzeltme Belgesi:** `docs/2209A_Eklenecek_Cikarilacak_ve_Kaynak_Kontrolu.docx`  
**Yazım İlkeleri:** `prompts/rapor_prompt.md` (AI kalıplarından arındırılmış, doğal insan ritminde, somut ve dengeli anlatım)

---

## Araştırma Başlığı
Eksik ve Bozulmuş Endüstriyel Sensör Verilerinde Sensör Hatası ile Süreç Anomalisinin Ayrı Değerlendirilmesi

## Anahtar Kelimeler
Endüstriyel Sensörler, Süreç Anomalisi, Sensör Bozulması, Yanlış Alarm Azaltma, SKAB Veri Kümesi

---

## Özet
Endüstriyel tesislerde makinelerin çalışmasını izlemek amacıyla çok sayıda sensörden kesintisiz veri toplanıyor. Sahadan gelen bir ölçümün beklenmedik değerler alması her zaman makinede fiziksel bir arıza başladığı anlamına gelmiyor; sensörde zamanla oluşan kalibrasyon kayması, temas zayıflığı, veri kaybı ya da elektriksel gürültü de sinyali bozabiliyor. İncelenen temel anomali tespit yöntemleri gelen veriyi tek bir girdi vektörü olarak ele aldığından, ölçüm hatasını süreç arızasından açık bir mekanizmayla ayıramıyor ve bakım ekiplerine gereksiz yanlış alarm yükü bindirebiliyor.

Bu araştırma, sensörün veri güvenilirliği ile makinenin fiziksel süreç durumunu ayrı koldan puanlayan hafif bir değerlendirme çerçevesinin katkısını incelemeyi amaçlıyor. Çalışmada Skoltech Anomaly Benchmark (SKAB) su sirkülasyon test standına ait çok değişkenli zaman serileri kullanılacak. Ham gözlemler değiştirilmeden; çalışma anında bellek üzerinde yavaş kayma, sinyal donması, gürültü sıçraması ve ardışık veri kaybı gibi sentetik bozulmalar uygulanacak. Sistem; korelasyonlu sensör çiftlerinin artık dinamiklerini izleyen bir güvenilirlik katmanı ile süreç durumunu puanlayan temel modelleri bir araya getirecek.

Araştırma kapsamında dört durum (normal süreç ve bozulma yok, normal süreç ve bozulma var, anomalili süreç ve bozulma yok, anomalili süreç ve bozulma var) bağımsız test serilerinde sınanacak. Yanlış alarm azalması, tekil örneklerin ötesinde olay yakalama oranı, algılama gecikmesi ve karar verilemeyen durumların sıklığıyla birlikte ele alınacak. Altı aylık çalışma takvimiyle açık kodlu, veri sızıntısından arındırılmış ve sentetik bozulmalar altındaki davranış sınırları şeffafça belgelenmiş bir değerlendirme protokolü sunulması hedefleniyor.

---

## 1.1. Konunun Önemi ve Araştırma Önerisinin Bilimsel Niteliği
Üretim hatlarında ve enerji altyapılarında beklenmedik duruşların önüne geçebilmek adına kestirimci bakım yaklaşımları yaygınlaşıyor. Bu sistemlerde titreşim, basınç, akış ve sıcaklık sensörleri makinenin anlık durumunu sürekli izliyor. Ancak fabrika ortamı sensörler için oldukça yıpratıcıdır; sıcaklık dalgalanmaları, elektromanyetik parazitler, kirlenme veya kablo hattındaki gevşemeler zamanla ölçüm hassasiyetini düşürüyor. Bir sıcaklık ölçümünün kademeli tırmanışı gerçekten motorun aşırı ısınmasından kaynaklanabileceği gibi, sensör elemanındaki basit bir direnç kaymasından da ileri gelebiliyor. Mevcut uygulamalarda sıkça başvurulan temel çok değişkenli yöntemler—örneğin İzolasyon Ormanı veya temel mesafe ölçütleri—gelen veriyi tek bir vektör olarak işlediği için, sensördeki yerel bir kayma veya geçici donma doğrudan makine arızası alarmına dönüşebiliyor.

Bu durum bakım ekiplerinde alarm yorgunluğu doğuruyor ve sahadaki operatörlerin uyarılara güvenini sarsıyor. Literatürde süreç ve sensör arızalarının birbirinden ayrılması daha önce araştırılmıştır; nitekim Zhang, Luo ve Dai (2021) kimya endüstrisinde dinamik çekirdek PCA ve katkı grafikleriyle bu ayrımı sağlayan bütünleşik bir çerçeve geliştirmiştir. Son dönem çalışmalarda Türkdamar ve Öztürk (2025), TEP ve SKAB verilerinde evrişimli ağlarla süreç anomali tespitini ele almış; Sun, Fan ve Wang (2024), endüstriyel arıza teşhisinde karşıt görevlerle desteklenen ardışık meta öğrenme önermiş; Teng ve Gao (2026) ise eksik gözlem, gürültü ve kayma koşullarında nedensel artık öğrenimi ve kapılama mimarisiyle alarm yükünü incelemiştir.

Geniş parametreli derin öğrenme veya karmaşık manifold yöntemlerinin aksine, bu projenin amacı literatürde zaten incelenmiş olan bu ayrımı ilk kez önermek değildir. Temel odağımız; kaynak tüketimi düşük, hafif ve yorumlanabilir bir sensör güvenilirliği katmanının, kontrollü sentetik bozulmalar ve bağımsız deneyler altında yanlış alarmları ne ölçüde bastırabildiğini deneysel olarak sınamaktır. Araştırma sorumuz şudur: Fiziksel tutarlılık temelli hafif bir güvenilirlik süzgeci, gerçek süreç anomalilerini yakalama başarısını ve algılama süresini zedelemeden yanlış süreç alarmlarını ne kadar azaltabilir? Çalışma, gerçek fabrika doğrulaması iddiası taşımamakta; sentetik müdahaleler altındaki anomali tespit dayanıklılığını ölçmeyi hedeflemektedir.

Öneri, T.C. Cumhurbaşkanlığı Strateji ve Bütçe Başkanlığı tarafından hazırlanan On İkinci Kalkınma Planı'nın (2024–2028) imalat sanayiinde dijital dönüşüm, büyük veri analitiği ve kestirimci bakım altyapılarının geliştirilmesine yönelik politika hedefleriyle uyumludur. Aynı zamanda T.C. Sanayi ve Teknoloji Bakanlığı'nın 2030 Sanayi ve Teknoloji Stratejisi belgesinde önceliklendirilen kritik teknoloji alanları, endüstriyel yapay zekâ ve güvenilir veri işleme eksenine katkı sağlamayı amaçlamaktadır.

---

## 1.2. Amaç ve Hedefler
Projenin temel amacı, endüstriyel sensör ölçümlerine kontrollü olarak eklenen yavaş kayma, donma, gürültü ve veri kaybı koşullarında, hafif bir sensör güvenilirliği katmanının yanlış süreç alarmlarını azaltma, gerçek arızaları yakalama ve algılama gecikmesi üzerindeki etkisini bağımsız test serilerinde deneysel olarak ortaya koymaktır.

Hedef 1: SKAB veri tabanındaki 35 adet çok değişkenli CSV dosyasının envanterini tamamlamak; zaman sırası ve etiket yapısı doğrulanmış serileri dosya kimlikleri üzerinden eğitim (anomaly-free), doğrulama (valve1 ve other serilerinden 6 dosya) ve test (20'den fazla bağımsız seri) gruplarına ayırmak.

Hedef 2: Ham gözlem verilerini değiştirmeden koruyarak; çalışma anında bellek üzerinde tekil sensörlere kontrollü yavaş kayma (drift), sinyal donması (stuck-at), gürültü sıçraması ve ardışık ölçüm kaybı uygulayabilen, rastgele tohum kontrollü bir sentetik bozulma ortamı geliştirmek.

Hedef 3: Fiziksel olarak korele çalışan sensör kanalları arasındaki ilişkiyi takip eden kural ve artık temelli hafif bir sensör güvenilirlik katmanı ile şüpheli kanalları izole eden süreç değerlendirme mekanizmasını kurmak.

Hedef 4: Geleneksel tek havuzlu anomali tespit yaklaşımı ile önerilen ayrık değerlendirme modelini aynı kontrollü bozulma senaryoları altında karşılaştırarak, yanlış alarm oranındaki değişimi sayısal olarak ortaya koymak.

Hedef 5: Bağımsız test serilerinde gerçek süreç anomalisi içeren aralıklarda arıza yakalama başarısının (olay ve örnek düzeyinde recall) takip edilmesini ve eşik optimizasyonuyla dengenin korunmasını sağlamak; algılama gecikmesindeki değişimi gerçek zaman damgaları üzerinden ölçmek.

Hedef 6: Tüm veri bölme kayıtlarını, bozulma senaryolarını, model kodlarını ve karşılaştırmalı değerlendirme çıktılarını açık kaynaklı bir GitHub deposunda eksiksiz belgeleyerek araştırmacıların erişimine sunmak.

---

## 2. Yöntem
Araştırma, açık kaynaklı Skoltech Anomaly Benchmark (SKAB) su sirkülasyon test düzeneği verileri üzerinde deneysel olarak yürütülecektir. Test düzeneği kapalı devre su boru hattı, santrifüj pompa, elektrik motoru ve vana gruplarından oluşmakta; 8 adet endüstriyel sensörden (2 titreşim ivmeölçeri RMS, motor akımı, gerilim, pompa çıkış basıncı, motor sıcaklığı, sıvı sıcaklığı ve hacimsel akış debisi) 1 Hz nominal frekansla veri toplamaktadır.

Çalışmanın bağımsız değişkenleri; uygulanan sentetik bozulmanın türü (yavaş kayma, sinyal donması, gürültü sıçraması, ardışık veri kaybı), bozulmanın şiddeti (eğitim verisinin standart sapmasına oranla 1-sigma ile 5-sigma arası), müdahale süresi ve hedef sensör kanalıdır. Bağımlı değişkenler ise üretilen yanlış süreç alarmı oranı (FAR), yanlış alarm olayı/saat frekansı, örnek ve olay düzeyinde arıza yakalama oranı (Recall), F1 skoru, algılama gecikmesi (saniye) ve sistemin karar veremediği durumların oranıdır (karar kapsama oranı).

1. Veri Bölme ve Test Verisinin Korunması: 
Yapılan envanter incelemesinde SKAB bünyesinde toplam 46.806 satır ve 35 CSV bulunduğu; hiçbir hücrede NaN değeri yer almadığı, ancak 7 dosyada nominal 1 saniyelik periyodu aşan (2 saniyenin üzerindeki) zaman boşlukları olduğu doğrulanmıştır. Veri sızıntısını önlemek amacıyla deney bazlı sabit bölme uygulanacaktır: 'anomaly-free.csv' (9.405 satır) temel eğitim için; 'valve1' ve 'other' gruplarından seçilen 6 dosya doğrulama ve eşik belirleme için; kalan 20'yi aşkın dosya ise bağımsız test için ayrılmıştır. İlk pilotta incelenen 'other/5' ve 'valve1/1' serileri nihai test kanıtı sayılmayacaktır. Aynı ham deneyden türetilen özgün ve bozulmuş tüm kopyalar aynı veri bölümünde tutulacak; test verileri ön işleme parametrelerinin öğrenilmesinde veya eşik ayarında kesinlikle kullanılmayacaktır.

2. Kontrollü Sentetik Bozulma Protokolü: 
Ham veriler değiştirilmeden korunacak; çalışma anında bellek üzerinde hedef sensör kanalına müdahale edilecektir. Dört bozulma türü incelenecektir: (a) Yavaş ölçüm kayması (eğitim standart sapmasının 1 ila 5 katı kademeli drift), (b) Sabit değerde kalma (stuck-at donma), (c) Anlık gürültü sıçraması (yüksek varyanslı Gauss gürültüsü), (d) Ardışık ölçüm kaybı (paket kaybını temsil eden boşluklar). Bozulmalar normal dönemlere, anomali başlangıcına ve anomali aralığına ayrı ayrı enjekte edilerek şu dört deney durumu sınanacaktır: Normal süreç ve bozulma yok; Normal süreç ve bozulma var; Anomalili süreç ve bozulma yok; Anomalili süreç ve bozulma var.

3. Sensör Güvenilirliği ve Süreç Karar Mekanizması: 
Sistem iki kademeli kurgulanacaktır. İlk kademe, fiziksel olarak korele çalışan sensör çiftleri (örneğin motor milindeki iki ivmeölçer veya debi-basınç ilişkisi) arasındaki dinamik tutarlılığı artık (residual) analiziyle izler. Bir sensör eğitim sınırlarının dışına çıkarken ilişkili ikiz sensör normal seyrini koruyorsa 'Yalnız Sensör Bozulması' kararı üretilir. İkinci kademe olan süreç modelinde ise şüpheli kanalın tüm sistemi yanıltmasını önlemek için ilgili kanal dışlanarak güvenilir süreç kanalları üzerinden eğitilmiş alt modeller devreye alınacaktır. Karar verilemeyecek kadar yüksek veri kaybı olduğunda sistem zorla tahmin üretmeyip 'Değerlendirilemiyor' çıktısı verecektir.

4. Karşılaştırma Hattı ve Adil Kıyaslama: 
Üç yaklaşım aynı test verilerinde kıyaslanacaktır: (i) Tüm sensörleri tek girdi kabul eden çok değişkenli temel yöntem (Mahalanobis mesafesi ve İzolasyon Ormanı), (ii) Yalnızca referans sensörü tek başına kullanan temel model, (iii) Önerilen sensör güvenilirliği katmanlı yöntem. Böylece sağlanan iyileşmenin sensör ayrıştırma mantığından mı yoksa tekil sensör seçiminden mi kaynaklandığı adil biçimde ayrıştırılacaktır.

5. Ön Çalışma ve Pilot Deney Bulguları: 
SKAB 'other/5' (rotor dengesizliği) deneyi üzerinde kural tabanlı bir başlangıç denemesi yapılmıştır. Birinci ivmeölçerin 120–319 örnek indekslerine doğrusal olarak 0–0,35 g kayma eklenmiştir. Bu bölgedeki 200 örneğin 191'inde (%95,5) temel yöntem süreç alarmı üretirken, ikinci ivmeölçerden süreç kanıtı arayan kural tabanlı başlangıç yaklaşımı aynı bölgede süreç alarmı üretmemiştir. Her iki yaklaşım, kaynak etiketi anomalili olan 410 örneğin tamamında (recall %100) alarm vermiştir. Ancak bu bulgu tek deney ve tek bozulma koşuluyla sınırlıdır; bağımsız deneylere genellenebilirlik, çoklu bozulmalar ve eşzamanlı hata koşulları proje kapsamında araştırılacaktır.

6. Değerlendirme Ölçütleri ve Olay Birleştirme: 
Örnek bazlı metriklerin yanında, birbirini izleyen alarmlar belirli bir zaman toleransıyla tek bir alarm olayına birleştirilecek; yanlış alarm frekansı (olay/saat), olay düzeyinde arıza yakalama oranı ve algılama gecikmesi gerçek zaman damgaları farkı üzerinden saniye cinsinden hesaplanacaktır. Deneyler en az 10 farklı rastgele tohumla tekrarlanarak belirsizlik aralıklarıyla sunulacaktır.

---

## 3.1. Çalışma Takvimi
- 1. Ay: SKAB veri tabanının envanterinin tamamlanması, dosya bazlı eğitim-doğrulama-test bölme planının sabitlenmesi ve veri yükleme modülünün kodlanması (Proje Yürütücüsü, %15)
- 2. Ay: Kontrollü sentetik bozulma motorunun (kayma, donma, gürültü ve ardışık veri kaybı) kodlanması ve tohum kontrollü birim testlerinin yapılması (Proje Yürütücüsü, %20)
- 3. Ay: Temel karşılaştırma modellerinin (tek havuzlu Mahalanobis mesafesi ve İzolasyon Ormanı) kurulması ve baz başarım metriklerinin çıkarılması (Proje Yürütücüsü, %20)
- 4. Ay: Korelasyonlu sensör çiftlerine dayalı güvenilirlik katmanı ile şüpheli kanal dışlama mimarisinin kodlanması ve doğrulanması (Proje Yürütücüsü, %20)
- 5. Ay: Eşzamanlı hata senaryoları, parametrik şiddet taramaları ve zaman boşluğu içeren seriler üzerinde dayanıklılık deneylerinin yapılması (Proje Yürütücüsü, %15)
- 6. Ay: Bağımsız test serilerinde nihai karşılaştırmalı değerlendirmenin yapılması, açık kaynak kod havuzunun belgelenmesi ve proje sonuçlarının derlenmesi (Proje Yürütücüsü, %10)

---

## 3.2. Risk Yönetimi
1. Risk: Gerçek süreç anomalisinin sensör hatası sanılarak bastırılması ve kritik bir makine arızasının kaçırılması riski.  
   Tedbir (B Planı): Süreç karar katmanında yalnızca tek bir sensöre güvenilmeyecek; diğer fiziksel sensörlerde eşzamanlı sapma görüldüğünde süreç alarmına öncelik veren güvenlik ağırlıklı hiyerarşik karar kuralı uygulanacaktır.
2. Risk: Referans olarak kabul edilen ikinci sensörün de bozulması veya çoklu sensör arızası yaşanması durumunda tutarlılık modelinin yanılması.  
   Tedbir (B Planı): İkili ilişkiler yerine çok değişkenli artık analizi izlenecek; sensörler arası tutarsızlık geneli kapsadığında veya veri yetersiz kaldığında sistem zorla normal kararı vermeyip 'Değerlendirilemiyor' bayrağı kaldıracaktır.
3. Risk: Sensörler arası ilişkinin doğrusal olmaması veya çalışma rejimine göre değişmesi sebebiyle doğrusal artık modelinin hatalı alarm üretmesi.  
   Tedbir (B Planı): Doğrusal regresyona ek olarak çekirdekli PCA (Kernel PCA) ve yerel k-en yakın komşu gibi doğrusal olmayan alternatifler doğrulama verisinde karşılaştırılacak ve en kararlı yapı seçilecektir.
4. Risk: Veri setinde yer alan 2 saniyenin üzerindeki zaman atlamalarının zaman serisi modellerinin pencereleme düzenini bozması.  
   Tedbir (B Planı): Zaman boşlukları yapay verilerle doldurulmayacak; atlama süresi nominal periyodun 3 katını aştığında zaman penceresi sıfırlanacak ve boşluk süresince durum belirsiz olarak etiketlenecektir.

---

## 3.3. Araştırma Olanakları
1. Kişisel Bilgisayar ve Geliştirme Ortamı (Intel Core i5 İşlemci, 16 GB RAM, SSD Depolama): Veri hazırlama betiklerinin koşturulması, sentetik bozulma simülasyonları, makine öğrenmesi modellerinin eğitimi, test koşuları ve grafiksel analizler.
2. Açık Kaynaklı Veri ve Yazılım Altyapısı (SKAB Veri Tabanı, Python 3.10+, Pandas, NumPy, Scikit-learn, Matplotlib, Git/GitHub): Çok değişkenli zaman serisi analizi, doğrusal ve çekirdekli modellerin kodlanması, sürüm kontrolü ve tekrarlanabilir deney arşivinin tutulması.
3. Üniversite Kütüphanesi ve Akademik Veri Tabanı Ağları (IEEE Xplore, ScienceDirect, Web of Science): Endüstriyel anomali tespiti, sensör güvenilirliği ve kestirimci bakım literatüründeki güncel makale ve konferans bildirilerinin temini.

---

## 4. Yaygın Etki
- Bilimsel / Akademik Çıktılar: Araştırma bulguları, endüstriyel veri kalitesi ve anomali tespiti alanında ulusal veya uluslararası düzeyde hakemli bir mühendislik konferansına (örneğin IEEE SIU veya benzeri organizasyonlar) bildiri olarak sunulmak üzere hazırlanacaktır. Deney protokolü, veri bölme manifestoları ve geliştirilen kodlar açık kaynaklı bir GitHub deposunda yayımlanarak araştırmacıların ve lisans öğrencilerinin erişimine açılacaktır.
- Ekonomik / Ticari / Sosyal Çıktılar: Önerilen yaklaşım, kestirimci bakım yazılımlarında hatalı sensör ölçümlerinden kaynaklanan gereksiz süreç alarmlarını azaltarak bakım ekiplerinin karar güvenilirliğini destekleme potansiyeli taşımaktadır. İleride endüstriyel IoT izleme yazılımlarına entegre edilebilecek hafif bir karar destek mantığı ortaya konulacaktır.
- Yeni Projeler Oluşturmaya Yönelik Çıktılar: Bu projede kurulacak sentetik bozulma ve ayrık değerlendirme altyapısı, ilerleyen aşamalarda TÜBİTAK 2209-B (Sanayiye Yönelik Lisans Araştırma Projeleri) veya TEKNOFEST yarışmalarına sunulacak gerçek zamanlı gömülü kestirimci bakım prototipleri için temel teşkil edecektir.

---

## 5. Belirtmek İstediğiniz Diğer Konular
SKAB 'other/5' (rotor dengesizliği) deneyi üzerinde kural tabanlı bir başlangıç demosu gerçekleştirilmiştir. Birinci ivmeölçerin 120–319 örnek indekslerine (başlangıçtan itibaren 126–336. saniyeler arasına) doğrusal olarak 0–0,35 g kayma eklenmiştir. Bu bölgedeki 200 örneğin 191'inde temel yöntem süreç alarmı üretirken, ikinci ivmeölçerden süreç kanıtı arayan kural tabanlı başlangıç yaklaşımı aynı bölgede süreç alarmı üretmemiştir. Her iki yaklaşım, kaynak etiketi anomalili olan 410 örneğin tamamında (600–1.028. saniyeler arası) alarm üretmiştir. Bulgular tek deney ve tek bozulma senaryosuyla sınırlı olup, bağımsız test gruplarına genellenebilirlik proje kapsamında araştırılacaktır. İlgili karşılaştırma grafiği `results/demo/pilot_demo_karsilastirma.png` dosyasında arşivlenmiştir.

---

## 6. EK-1: Kaynaklar
1. Katser, I. D., & Kozitsin, V. O. (2020). Skoltech Anomaly Benchmark (SKAB). Kaggle. https://doi.org/10.34740/KAGGLE/DSV/1693952
2. Türkdamar, M. U., & Öztürk, C. (2025). Anomaly Detection on Industrial Processes with Convolutional Neural Networks. CAIAC 2025 Bildiriler Kitabı, 29.
3. Sun, D., Fan, Y., & Wang, G. (2024). Enhancing Fault Diagnosis in Industrial Processes through Adversarial Task Augmented Sequential Meta-Learning. Applied Sciences, 14(11), 4433. https://doi.org/10.3390/app14114433
4. Teng, S., & Gao, X. (2026). Causal Wavelet Residual Learning with Observation-Support Gating for Industrial Sensor Anomaly Detection. Sensors, 26(18), 5751. https://doi.org/10.3390/s26185751
5. Zhang, J., Luo, W., & Dai, Y. (2021). Integrated Diagnostic Framework for Process and Sensor Faults in Chemical Industry. Sensors, 21(3), 822. https://doi.org/10.3390/s21030822
6. Liu, F. T., Ting, K. M., & Zhou, Z. H. (2008). Isolation Forest. 2008 Eighth IEEE International Conference on Data Mining, 413–422. https://doi.org/10.1109/ICDM.2008.17
7. Hotelling, H. (1947). Multivariate Quality Control Illustrated by the Air Testing of Sample Bombsights. Techniques of Statistical Analysis, 111–184.
8. T.C. Cumhurbaşkanlığı Strateji ve Bütçe Başkanlığı. (2023). On İkinci Kalkınma Planı (2024–2028). Ankara.
9. T.C. Sanayi ve Teknoloji Bakanlığı. (2025). 2030 Sanayi ve Teknoloji Stratejisi. Ankara.
