# Proje Kararları ve Terminoloji Referansı (Decisions Log)

**Tarih:** 28 Ekim 2026  
**Bağlam:** TÜBİTAK 2209-A Araştırma Önerisi ve Pilot Altyapı Hazırlığı  
**Dayanak:** `pdf's/26.10.2026.pdf` (Karar Metni) ve `pdf's/2209A_03_Endustriyel_Sensor_Detayli_Taslak_Makaleli-2.pdf`

---

## 1. Terminoloji ve Kavramsal Ayrım

- **Süreç:** Makinenin veya endüstriyel sistemin fiziksel çalışması.
- **Süreç Anomalisi:** Sürecin beklenen fiziksel çalışma davranışından sapması.
- **Sensör/Veri Sorunu:** Ölçüm, kayıt veya aktarım kaynaklı bozulma şüphesi (donma, kayma, gürültü, paket kaybı).
- **Temel Ayrım:** "Süreç anomalisi" ile "veri hatası" kesinlikle eşanlamlı kullanılmaz. Gerçek bir makine arızasını doğru ölçen sensör, süreç açısından anormal veri üretse de ölçüm açısından doğrudur.
- **Kaynak Etiketi:** Veri setinin yayımlayıcısı tarafından sağlanan orijinal etiket (`anomaly`, `changepoint`).
- **Senaryo Etiketi:** Kontrollü deneyde yazılımla uygulanan sentetik müdahalenin kaydı.
- **Model Tahmini:** Modelin verilerden çıkardığı sonuç (asla kesin gerçek etiket olarak adlandırılamaz).
- **İnceleme Sonucu:** İnsan incelemesi sonrası kaydedilen nihai karar.

---

## 2. Alınan Mimari ve Metodolojik Kararlar

1. **Ham Verinin Dokunulmazlığı:** Ham SKAB CSV dosyaları hiçbir şekilde modifiye edilmez; temizleme veya sentetik bozulma işlemleri bağımsız kopyalar ve bellek içi akışlar üzerinden yürütülür.
2. **Deney/Seri Bazlı Bölme İlkesi:** Zaman serisi dosyaları rastgele satır bazında parçalanmaz. Bölünme dosya/deney seviyesinde yapılır. Bir temel deneyden türetilen tüm sentetik kopyalar aynı bölümde (eğitim, doğrulama veya test) kalır.
3. **Test Verisinin Mutlak Korunması:** Test verisi model seçimi, eşik belirleme veya ön işleme parametreleri çıkarmak için kesinlikle kullanılmaz.
4. **Olasılık ve Skor İlkesi:** Model anomali skorları kalibrasyon yapılmadan doğrudan "% olasılık" olarak sunulmaz. Yetersiz kanıt durumunda sistemin zorla 0 veya 1 seçmesi yerine *"Değerlendirilemiyor"* çıktısı üretmesi desteklenir.
5. **Dörtlü Değerlendirme Çerçevesi:**
   - (0, Yok): Normal süreç, sağlam sensör
   - (0, Var): Normal süreç, bozuk sensör
   - (1, Yok): Süreç anomalisi, sağlam sensör
   - (1, Var): Süreç anomalisi ve bozuk sensör birlikte

---

## 3. İlk Aşama Durumu
- **Aşama:** Veri Seçimi ve İnceleme (Tamamlandı).
- **Sonraki Adım:** Kullanıcı/Danışman kararları doğrultusunda Veri Bölme Planı ve Kontrollü Bozulma Ortamı tasarımı.
