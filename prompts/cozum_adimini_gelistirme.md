sana az önce bahsettiğim çözüm adımını şöyle güncelleyelim o zaman şimdi sana adım adım anlatacağım sonrasında seninle üstüne tartışacağız ve nihai çözüme ulaşmayı hedefleyeceğiz.

başlıyorum;



1. internet üzerinde projeye uygunluğu olan veri setleri toplanır ve incelenir
2. uygun olanlar toplanır ve filtreleme yapılır
3. filtrelemeden sonra etiketleme yapılır
4. etiketleme işleminden sonra sanal test ortamları (makine simülasyonu, sensor simülasyonu ve bunların verileriyle oynanabilecek bir ortam) oluşturulur 
5. sanal test ortamları ilk başta elle test edilir 
6. elle yapılan testlerde istenen başarı yakalanırsa model etiketlenmiş verilerle eğitilmeye başlanır
7. model eğitilirken sürekli öğrenecek şekilde tasarlanır 
8. sürekli öğrenme türü her aldığı veriyi modeli eğitmek için kullanmak değil bunun yerine sistem kalibre etmesi işleminden sonra sistem kendi içerisinde veri karşılaştırması yapmak adına bir eşik değer belirler
9. bu belirlediği eşik değer skoru üzerinden her aldığı yeni veri sonucunda bir kullanılabilir, kullanılamaz, hatalı sensor verisi, hatalı süreç verisi, doğru sensor verisi, doğru süreç verisi şeklinde etiketleme yapar ve geliştiriciye belli bir döngüde feedback atar
10. yapılan feedback sonucunda geliştirici gerekli kontrolleri sağlayıp yeni gelen verilerin doğruluğundan ve kesinliğinden emin olduktan sonrasında modeli geliştirmek için bu verileri kullanıma alabilir 
11. model eğitimi bittikten sonra test edilir ve istenen başarı sağlandıysa sanal test ortamında teste tabi tutulur
12. kurulan genel sistem üzerinde beklenen çıktı tipi ;Süreç normal - sensör sağlam,  Yalnız süreç sorunu , Yalnız sensör sorunu , Süreç ve sensör sorunu birlikte 
13. istenen çıktılar şeklinde kontrolcüye bir çıktı verilir



