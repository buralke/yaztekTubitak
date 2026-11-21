import os
from playwright.sync_api import sync_playwright

html_content = """<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<title>TÜBİTAK 2209-A TYBS Başvuru Sistemi Güncelleme Metinleri</title>
<style>
  @page {
    size: A4;
    margin: 18mm 15mm 18mm 15mm;
    @bottom-right {
      content: counter(page) " / " counter(pages);
      font-size: 8pt;
      color: #64748b;
    }
  }
  body {
    font-family: 'Segoe UI', Arial, Helvetica, sans-serif;
    color: #1e293b;
    line-height: 1.5;
    font-size: 9.5pt;
    margin: 0;
    padding: 0;
  }
  .header-card {
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
    color: white;
    padding: 20px 24px;
    border-radius: 8px;
    margin-bottom: 20px;
  }
  .header-card h1 {
    font-size: 16pt;
    margin: 0 0 6px 0;
    font-weight: 700;
    letter-spacing: -0.3px;
    color: #f8fafc;
  }
  .header-card p {
    margin: 3px 0;
    font-size: 9.5pt;
    color: #cbd5e1;
  }
  .badge {
    display: inline-block;
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 8pt;
    font-weight: 600;
    background: #e0f2fe;
    color: #0369a1;
    margin-bottom: 6px;
  }
  .alert-box {
    background-color: #fef2f2;
    border-left: 4px solid #ef4444;
    padding: 10px 14px;
    margin-bottom: 18px;
    border-radius: 0 6px 6px 0;
    font-size: 9pt;
    color: #991b1b;
  }
  .section-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 16px 18px;
    margin-bottom: 16px;
    page-break-inside: avoid;
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
  }
  .section-title {
    font-size: 11pt;
    font-weight: 700;
    color: #0f172a;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 6px;
    margin-top: 0;
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .tybs-tag {
    font-size: 8pt;
    background: #f1f5f9;
    color: #475569;
    padding: 2px 7px;
    border-radius: 4px;
    font-weight: 600;
  }
  .copy-text {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 12px 14px;
    font-size: 9pt;
    color: #0f172a;
    white-space: pre-wrap;
    word-break: break-word;
    margin-top: 6px;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 8px;
    font-size: 8.5pt;
  }
  th, td {
    border: 1px solid #cbd5e1;
    padding: 7px 9px;
    text-align: left;
    vertical-align: top;
  }
  th {
    background-color: #f1f5f9;
    font-weight: 600;
    color: #334155;
  }
  tr:nth-child(even) td {
    background-color: #f8fafc;
  }
  .note {
    font-size: 8.5pt;
    color: #64748b;
    font-style: italic;
    margin-top: 4px;
  }
  .page-break {
    page-break-before: always;
  }
</style>
</head>
<body>

<div class="header-card">
  <div class="badge">TÜBİTAK 2209-A BAŞVURU REHBERİ</div>
  <h1>TYBS PORTALI GÜNCELLENECEK TAM METİNLER REHBERİ</h1>
  <p><strong>Proje Başlığı:</strong> Eksik ve Bozulmuş Endüstriyel Sensör Verilerinde Sensör Hatası ile Süreç Anomalisinin Ayrı Değerlendirilmesi</p>
  <p><strong>Yürütücü:</strong> Burak ERDOĞAN | <strong>Danışman:</strong> Rukiye Nur KAÇMAZ</p>
  <p><strong>Kurum / Bölüm:</strong> Erciyes Üniversitesi, Mühendislik Fakültesi, Yazılım Mühendisliği Bölümü - KAYSERİ</p>
  <p><strong>Son Revizyon:</strong> 21 Kasım 2026 (Hakem/Hoca Geri Bildirimlerine Göre Tüm Hatalar Düzeltilmiş Nihai Sürüm)</p>
</div>

<div class="alert-box">
  <strong>⚠️ ÖNEMLİ KULLANIM NOTU:</strong> Bu belgedeki metinler; marka/kurum isimlerinin anonimleştirilmesi, bütçe çelişkilerinin giderilmesi, analitik artıklık literatürünün eklenmesi ve zaman kiplerinin akademik geniş zamana uyarlanmasıyla hazırlanmıştır. TYBS başvuru ekranında ilgili kutucukları doğrudan bu metinlerle güncelleyebilirsiniz.
</div>

<!-- ALAN 1: GENEL BİLGİLER VE KONTROL LİSTESİ -->
<div class="section-card">
  <div class="section-title">
    <span>1. GENEL BİLGİLER VE SEÇİMLER KONTROL LİSTESİ</span>
    <span class="tybs-tag">TYBS: Başvuru Bilgileri Ekranı</span>
  </div>
  <table>
    <tr><th style="width: 30%;">TYBS Alanı</th><th>Sistemde Seçilecek / Girilecek Doğru Bilgi</th></tr>
    <tr><td><strong>Başvuru Sahibi</strong></td><td>Burak ERDOĞAN</td></tr>
    <tr><td><strong>Proje Başlığı</strong></td><td>Eksik ve Bozulmuş Endüstriyel Sensör Verilerinde Sensör Hatası ile Süreç Anomalisinin Ayrı Değerlendirilmesi</td></tr>
    <tr><td><strong>Danışman Bilgisi</strong></td><td>Rukiye Nur KAÇMAZ</td></tr>
    <tr><td><strong>Üniversite / Fakülte / Bölüm</strong></td><td>Erciyes Üniversitesi / Mühendislik Fakültesi / Yazılım Mühendisliği Bölümü - KAYSERİ</td></tr>
    <tr><td><strong>Faaliyet Alanı / Tema</strong></td><td>Bilgi ve İletişim Teknolojileri &gt; Yapay Zekâ / Büyük Veri / Kestirimci Bakım</td></tr>
    <tr><td><strong>Etik Kurul Onay Belgesi</strong></td><td><strong>GEREKMİYOR.</strong> (Sistemde "Muaf / Gerekmemektedir" seçilecek. Açık kaynaklı laboratuvar kıyaslama verisi kullanıldığı için insan/hayvan deneyi yoktur.)</td></tr>
  </table>
</div>

<!-- ALAN 2: ÖZET VE ANAHTAR KELİMELER -->
<div class="section-card">
  <div class="section-title">
    <span>2. ÖZET VE ANAHTAR KELİMELER</span>
    <span class="tybs-tag">TYBS: Özet Ekranı</span>
  </div>
  <p><strong>Özet Metni:</strong></p>
  <div class="copy-text">Endüstriyel tesislerde makinelerin çalışmasını izlemek amacıyla çok sayıda sensörden kesintisiz veri toplanmaktadır. Sahadan gelen bir ölçümün beklenmedik değerler alması her zaman makinede fiziksel bir arıza başladığı anlamına gelmemektedir; sensörde zamanla oluşan kalibrasyon kayması, temas zayıflığı, veri kaybı ya da elektriksel gürültü de sinyali bozabilmektedir. İncelenen temel anomali tespit yöntemleri gelen veriyi tek bir girdi vektörü olarak ele aldığından, ölçüm hatasını süreç arızasından açık bir mekanizmayla ayıramamakta ve bakım ekiplerine gereksiz yanlış alarm yükü bindirmektedir.

Bu araştırma, sensörün veri güvenilirliği ile makinenin fiziksel süreç durumunu ayrı koldan puanlayan hafif bir değerlendirme çerçevesinin katkısını incelemeyi amaçlamaktadır. Çalışmada Skoltech Anomaly Benchmark (SKAB; Katser ve Kozitsin, 2020) su sirkülasyon test standına ait çok değişkenli zaman serileri kullanılacaktır. Ham gözlemler değiştirilmeden; çalışma anında bellek üzerinde yavaş kayma, sinyal donması, gürültü sıçraması ve ardışık veri kaybı gibi sentetik bozulmalar uygulanacaktır. Sistem; korelasyonlu sensör çiftlerinin artık dinamiklerini izleyen bir güvenilirlik katmanı ile süreç durumunu puanlayan temel modelleri bir araya getirecektir.

Araştırma kapsamında dört durum (normal süreç ve bozulma yok, normal süreç ve bozulma var, anomalili süreç ve bozulma yok, anomalili süreç ve bozulma var) bağımsız test serilerinde sınanacaktır. Yanlış alarm azalması, tekil örneklerin ötesinde olay yakalama oranı, algılama gecikmesi ve karar verilemeyen durumların sıklığıyla birlikte ele alınacaktır. Altı aylık çalışma takvimiyle açık kodlu, veri sızıntısından arındırılmış ve sentetik bozulmalar altındaki davranış sınırları şeffafça belgelenmiş bir değerlendirme protokolü sunulması hedeflenmektedir.</div>

  <p style="margin-top: 10px; margin-bottom: 4px;"><strong>Anahtar Kelimeler:</strong></p>
  <div class="copy-text">Endüstriyel Sensörler, Süreç Anomalisi, Sensör Bozulması, Yanlış Alarm Azaltma, SKAB Veri Kümesi</div>
</div>

<div class="page-break"></div>

<!-- ALAN 3: 1.1 BİLİMSEL NİTELİK -->
<div class="section-card">
  <div class="section-title">
    <span>3. 1.1. KONUNUN ÖNEMİ VE ARAŞTIRMA ÖNERİSİNİN BİLİMSEL NİTELİĞİ</span>
    <span class="tybs-tag">TYBS: Bilimsel Nitelik Ekranı</span>
  </div>
  <p class="note">Not: Klasik analitik artıklık (Dunia ve Qin, 1996; Gertler, 1998) literatürü eklenmiş, Teng & Gao (2026) ile olan fark netleştirilmiş, Kalkınma Planı ve Strateji atıfları eklenmiştir.</p>
  <div class="copy-text">Üretim hatlarında ve enerji altyapılarında beklenmedik duruşların önüne geçebilmek adına kestirimci bakım yaklaşımları yaygınlaşmaktadır. Bu sistemlerde titreşim, basınç, akış ve sıcaklık sensörleri makinenin anlık durumunu sürekli izlemektedir. Ancak fabrika ortamı sensörler için oldukça yıpratıcıdır; sıcaklık dalgalanmaları, elektromanyetik parazitler, kirlenme veya kablo hattındaki gevşemeler zamanla ölçüm hassasiyetini düşürmektedir. Bir sıcaklık ölçümünün kademeli tırmanışı gerçekten motorun aşırı ısınmasından kaynaklanabileceği gibi, sensör elemanındaki basit bir direnç kaymasından da ileri gelebilmektedir. Mevcut uygulamalarda sıkça başvurulan temel çok değişkenli yöntemler—örneğin İzolasyon Ormanı (Liu ve ark., 2008) veya Mahalanobis mesafesi (Mahalanobis, 1936)—gelen veriyi tek bir vektör olarak işlediği için, sensördeki yerel bir kayma veya geçici donma doğrudan makine arızası alarmına dönüşebilmektedir.

Bu durum bakım ekiplerinde alarm yorgunluğu doğurmakta ve sahadaki operatörlerin uyarılara güvenini sarsmaktadır. Literatürde süreç ve sensör arızalarının birbirinden ayrılması klasik hata tespit ve izolasyon (FDI) ile analitik artıklık (analytical redundancy) modellerine dayanmaktadır (Gertler, 1998; Dunia ve Qin, 1996). Nitekim Zhang, Luo ve Dai (2021) kimya endüstrisinde dinamik çekirdek PCA ve katkı grafikleriyle bu ayrımı sağlayan bütünleşik bir çerçeve geliştirmiştir. Son dönem çalışmalarda Türkdamar ve Öztürk (2025), TEP ve SKAB (Katser ve Kozitsin, 2020) verilerinde evrişimli ağlarla süreç anomali tespitini ele almış; Sun, Fan ve Wang (2024), endüstriyel arıza teşhisinde karşıt görevlerle desteklenen ardışık meta öğrenme önermiştir. Çalışmamıza en yakın güncel literatür olan Teng ve Gao (2026) ise eksik gözlem, gürültü ve kayma koşullarında nedensel artık öğrenimi ve kapılama mimarisiyle alarm yükünü incelemiştir. Ancak Teng ve Gao (2026) öğrenilmiş derin ve parametre yoğun bir kapılama mekanizması kullanırken; bu araştırma önerisi eğitimsiz, fiziksel ikiz-sensör dinamik tutarlılığına dayalı, hesaplama maliyeti düşük ve yorumlanabilir bir güvenilirlik katmanı önermektedir. Dahası, tek bir birleşik anomali skoru yerine sensör güvenilirliği ile süreç kararını bağımsız çıktılar olarak ayrıştırmakta ve sahadaki personele sensör hatası ile süreç arızasını şeffaf biçimde raporlamaktadır.

Bu proje, söz konusu ayrımı ilk kez önermeyi değil; derin ve parametre yoğun yöntemlere alternatif olarak hafif ve yorumlanabilir bir güvenilirlik katmanının etkisini kontrollü sentetik bozulmalar altında sınamayı amaçlamaktadır. Temel odağımız; kaynak tüketimi düşük bir sensör güvenilirliği süzgecinin, bağımsız test serilerinde yanlış süreç alarmlarını ne ölçüde bastırabildiğini deneysel olarak ortaya koymaktır. Araştırma sorumuz şudur: Fiziksel tutarlılık temelli hafif bir güvenilirlik süzgeci, gerçek süreç anomalilerini yakalama başarısını ve algılama süresini zedelemeden yanlış süreç alarmlarını ne kadar azaltabilir? Çalışma, gerçek fabrika doğrulaması iddiası taşımamakta; sentetik müdahaleler altındaki anomali tespit dayanıklılığını ölçmeyi hedeflemektedir.

Öneri, T.C. Cumhurbaşkanlığı Strateji ve Bütçe Başkanlığı (2023) tarafından hazırlanan On İkinci Kalkınma Planı'nın (2024–2028) imalat sanayiinde dijital dönüşüm, büyük veri analitiği ve kestirimci bakım altyapılarının geliştirilmesine yönelik politika hedefleriyle uyumludur. Aynı zamanda T.C. Sanayi ve Teknoloji Bakanlığı (2025) tarafından yayımlanan 2030 Sanayi ve Teknoloji Stratejisi belgesinde önceliklendirilen kritik teknoloji alanları, endüstriyel yapay zekâ ve güvenilir veri işleme eksenine doğrudan katkı sağlamayı amaçlamaktadır.</div>
</div>

<!-- ALAN 4: 1.2 AMAÇ VE HEDEFLER -->
<div class="section-card">
  <div class="section-title">
    <span>4. 1.2. AMAÇ VE HEDEFLER</span>
    <span class="tybs-tag">TYBS: Amaç ve Hedefler Ekranı</span>
  </div>
  <div class="copy-text">Projenin temel amacı, endüstriyel sensör ölçümlerine kontrollü olarak eklenen yavaş kayma, donma, gürültü ve veri kaybı koşullarında, hafif bir sensör güvenilirliği katmanının yanlış süreç alarmlarını azaltma, gerçek arızaları yakalama ve algılama gecikmesi üzerindeki etkisini bağımsız test serilerinde deneysel olarak ortaya koymaktır.

Hedef 1: SKAB veri kümesindeki 35 adet çok değişkenli CSV dosyasının envanterini tamamlamak; zaman sırası ve etiket yapısı doğrulanmış serileri dosya kimlikleri üzerinden eğitim (anomaly-free), doğrulama (valve1 ve other serilerinden 6 dosya) ve test (20'den fazla bağımsız seri) gruplarına ayırmak.

Hedef 2: Ham gözlem verilerini değiştirmeden koruyarak; çalışma anında bellek üzerinde tekil sensörlere kontrollü yavaş kayma (drift), sinyal donması (stuck-at), gürültü sıçraması ve ardışık ölçüm kaybı uygulayabilen, rastgele tohum kontrollü bir sentetik bozulma ortamı geliştirmek.

Hedef 3: Fiziksel olarak korele çalışan sensör kanalları arasındaki ilişkiyi takip eden kural ve artık temelli hafif bir sensör güvenilirlik katmanı ile şüpheli kanalları izole eden süreç değerlendirme mekanizmasını kurmak.

Hedef 4: Geleneksel tek havuzlu anomali tespit yaklaşımı ile önerilen ayrık değerlendirme modelini aynı kontrollü bozulma senaryoları altında karşılaştırarak, yanlış alarm oranındaki değişimi sayısal olarak ortaya koymak.

Hedef 5: Bağımsız test serilerinde gerçek süreç anomalisi içeren aralıklarda arıza yakalama başarısının (olay ve örnek düzeyinde recall) takip edilmesini ve eşik optimizasyonuyla dengenin korunmasını sağlamak; algılama gecikmesindeki değişimi gerçek zaman damgaları üzerinden ölçmek.

Hedef 6: Tüm veri bölme kayıt dosyalarını, bozulma senaryolarını, model kodlarını ve karşılaştırmalı değerlendirme çıktılarını açık erişimli ve sürüm kontrollü bir kod deposunda eksiksiz belgeleyerek araştırmacıların erişimine sunmak.</div>
</div>

<div class="page-break"></div>

<!-- ALAN 5: 2. YÖNTEM -->
<div class="section-card">
  <div class="section-title">
    <span>5. 2. YÖNTEM</span>
    <span class="tybs-tag">TYBS: Yöntem Ekranı</span>
  </div>
  <div class="copy-text">Araştırma, açık kaynaklı Skoltech Anomaly Benchmark (SKAB; Katser ve Kozitsin, 2020) su sirkülasyon test düzeneği verileri üzerinde deneysel olarak yürütülecektir. Test düzeneği kapalı devre su boru hattı, santrifüj pompa, elektrik motoru ve vana gruplarından oluşmakta; 8 adet endüstriyel sensörden (2 titreşim ivmeölçeri RMS, motor akımı, gerilim, pompa çıkış basıncı, motor sıcaklığı, sıvı sıcaklığı ve hacimsel akış debisi) 1 Hz nominal frekansla veri toplamaktadır.

Çalışmanın bağımsız değişkenleri; uygulanan sentetik bozulmanın türü (yavaş kayma, sinyal donması, gürültü sıçraması, ardışık veri kaybı), bozulmanın şiddeti (eğitim verisinin standart sapmasına oranla 1-sigma ile 5-sigma arası), müdahale süresi ve hedef sensör kanalıdır. Bağımlı değişkenler ise üretilen yanlış süreç alarmı oranı (FAR), yanlış alarm olayı/saat frekansı, örnek ve olay düzeyinde arıza yakalama oranı (Recall), F1 skoru, algılama gecikmesi (saniye) ve sistemin karar veremediği durumların oranıdır (karar kapsama oranı).

1. Veri Bölme ve Test Verisinin Korunması: Yapılan envanter incelemesinde SKAB veri kümesi bünyesinde toplam 46.806 satır ve 35 CSV bulunduğu; hiçbir hücrede NaN değeri yer almadığı, ancak 7 dosyada nominal 1 saniyelik periyodu aşan (2 saniyenin üzerindeki) zaman boşlukları olduğu doğrulanmıştır. Veri sızıntısını önlemek amacıyla deney bazlı sabit bölme uygulanacaktır: 'anomaly-free.csv' (9.405 satır) temel eğitim için; 'valve1' ve 'other' gruplarından seçilen 6 dosya doğrulama ve eşik belirleme için; kalan 20'yi aşkın dosya ise bağımsız test için ayrılmıştır. İlk pilotta incelenen 'other/5' ve 'valve1/1' serileri nihai test kanıtı sayılmayacaktır. Aynı ham deneyden türetilen özgün ve bozulmuş tüm kopyalar aynı veri bölümünde tutulacak; test verileri ön işleme parametrelerinin öğrenilmesinde veya eşik ayarında kesinlikle kullanılmayacaktır.

2. Kontrollü Sentetik Bozulma Protokolü: Ham veriler değiştirilmeden korunacak; çalışma anında bellek üzerinde hedef sensör kanalına müdahale edilecektir. Dört bozulma türü incelenecektir: (a) Yavaş ölçüm kayması (eğitim standart sapmasının 1 ila 5 katı kademeli drift), (b) Sabit değerde kalma (stuck-at donma), (c) Anlık gürültü sıçraması (yüksek varyanslı Gauss gürültüsü), (d) Ardışık ölçüm kaybı (paket kaybını temsil eden boşluklar). Bozulmalar normal dönemlere, anomali başlangıcına ve anomali aralığına ayrı ayrı enjekte edilerek şu dört deney durumu sınanacaktır: Normal süreç ve bozulma yok; Normal süreç ve bozulma var; Anomalili süreç ve bozulma yok; Anomalili süreç ve bozulma var.

3. Sensör Güvenilirliği ve Süreç Karar Mekanizması: Sistem iki kademeli kurgulanacaktır. İlk kademe, fiziksel olarak korele çalışan sensör çiftleri (örneğin motor milindeki iki ivmeölçer veya debi-basınç ilişkisi) arasındaki dinamik tutarlılığı artık (residual) analiziyle izler. Bir sensör eğitim sınırlarının dışına çıkarken ilişkili ikiz sensör normal seyrini koruyorsa 'Yalnız Sensör Bozulması' kararı üretilir. İkinci kademe olan süreç modelinde ise şüpheli kanalın tüm sistemi yanıltmasını önlemek için ilgili kanal dışlanarak güvenilir süreç kanalları üzerinden eğitilmiş alt modeller devreye alınacaktır. Karar verilemeyecek kadar yüksek veri kaybı olduğunda sistem zorla tahmin üretmeyip 'Değerlendirilemiyor' çıktısı verecektir.

4. Karşılaştırma Hattı ve Adil Kıyaslama: Üç yaklaşım aynı test verilerinde kıyaslanacaktır: (i) Tüm sensörleri tek girdi kabul eden çok değişkenli temel yöntemler (Mahalanobis mesafesi [Mahalanobis, 1936] ve İzolasyon Ormanı [Liu ve ark., 2008]), (ii) Yalnızca referans sensörü tek başına kullanan temel model, (iii) Önerilen sensör güvenilirliği katmanlı yöntem. Böylece sağlanan iyileşmenin sensör ayrıştırma mantığından mı yoksa tekil sensör seçiminden mi kaynaklandığı adil biçimde ayrıştırılacaktır.

5. Ön Çalışma ve Pilot Deney Bulguları: SKAB 'other/5' (rotor dengesizliği) deneyi üzerinde kural tabanlı bir başlangıç denemesi yapılmıştır. Birinci ivmeölçerin 120–319 örnek indekslerine doğrusal olarak 0–0,35 g kayma eklenmiştir. Bu bölgedeki 200 örneğin 191'inde (%95,5) temel yöntem süreç alarmı üretirken, ikinci ivmeölçerden süreç kanıtı arayan kural tabanlı başlangıç yaklaşımı aynı bölgede süreç alarmı üretmemiştir. Her iki yaklaşım, kaynak etiketi anomalili olan 410 örneğin tamamında (recall %100) alarm vermiştir. Ancak bu bulgu tek deney ve tek bozulma koşuluyla sınırlıdır; bağımsız deneylere genellenebilirlik, çoklu bozulmalar ve eşzamanlı hata koşulları proje kapsamında araştırılacaktır.

6. Değerlendirme Ölçütleri ve Olay Birleştirme: Örnek bazlı metriklerin yanında, birbirini izleyen alarmlar belirli bir zaman toleransıyla tek bir alarm olayına birleştirilecek; yanlış alarm frekansı (olay/saat), olay düzeyinde arıza yakalama oranı ve algılama gecikmesi gerçek zaman damgaları farkı üzerinden saniye cinsinden hesaplanacaktır. Deneyler en az 10 farklı rastgele tohumla tekrarlanarak belirsizlik aralıklarıyla sunulacaktır.</div>
</div>

<div class="page-break"></div>

<!-- ALAN 6: 3.1 ÇALIŞMA TAKVİMİ -->
<div class="section-card">
  <div class="section-title">
    <span>6. 3.1. ÇALIŞMA TAKVİMİ</span>
    <span class="tybs-tag">TYBS: Çalışma Takvimi Ekranı</span>
  </div>
  <p class="note">Not: "1, 1, 1, 1, 1, 1" karışıklığı giderilmiş; faaliyet ayları netleştirilmiştir.</p>
  <table>
    <tr>
      <th style="width: 14%;">Proje Süresi (Ay)</th>
      <th style="width: 36%;">Faaliyetler</th>
      <th style="width: 24%;">Kim(ler) Tarafından Gerçekleştirileceği</th>
      <th style="width: 26%;">Başarı Ölçütü ve Katkısı</th>
    </tr>
    <tr>
      <td><strong>1. Ay</strong></td>
      <td>SKAB veri kümesinin envanterinin tamamlanması, dosya bazlı eğitim-doğrulama-test bölme planının sabitlenmesi ve veri yükleme modülünün kodlanması</td>
      <td>Burak ERDOĞAN (Danışman gözetiminde)</td>
      <td>35 veri dosyasının deney bazlı ayrımının tamamlanması ve veri sızıntısı içermeyen yükleyici modülün doğrulanması (%15)</td>
    </tr>
    <tr>
      <td><strong>2. Ay</strong></td>
      <td>Kontrollü sentetik bozulma motorunun (kayma, donma, gürültü ve ardışık veri kaybı) kodlanması ve tohum kontrollü birim testlerinin yapılması</td>
      <td>Burak ERDOĞAN (Danışman gözetiminde)</td>
      <td>Ham veriyi değiştirmeden bellek üzerinde 4 farklı sentetik bozulmayı deterministik üreten modülün testlerinin tamamlanması (%20)</td>
    </tr>
    <tr>
      <td><strong>3. Ay</strong></td>
      <td>Temel karşılaştırma modellerinin (tek havuzlu Mahalanobis mesafesi ve İzolasyon Ormanı) kurulması ve baz başarım metriklerinin çıkarılması</td>
      <td>Burak ERDOĞAN (Danışman gözetiminde)</td>
      <td>Temel modellerin eğitim verisinde eğitilip, sentetik bozulma altındaki yanlış alarm ve gecikme metriklerinin kaydedilmesi (%20)</td>
    </tr>
    <tr>
      <td><strong>4. Ay</strong></td>
      <td>Korelasyonlu sensör çiftlerine dayalı güvenilirlik katmanı ile şüpheli kanal dışlama mimarisinin kodlanması ve doğrulanması</td>
      <td>Burak ERDOĞAN (Danışman gözetiminde)</td>
      <td>Sensör güvenilirlik katmanının entegre edilerek dört durumlu karar mekanizmasının çalışır hale getirilmesi (%20)</td>
    </tr>
    <tr>
      <td><strong>5. Ay</strong></td>
      <td>Eşzamanlı hata senaryoları, parametrik şiddet taramaları ve zaman boşluğu içeren seriler üzerinde dayanıklılık deneylerinin yapılması</td>
      <td>Burak ERDOĞAN (Danışman gözetiminde)</td>
      <td>Farklı kayma ve gürültü seviyelerinde 10 tekrarlı koşuların tamamlanıp yanlış alarm ve olay yakalama verilerinin çıkarılması (%15)</td>
    </tr>
    <tr>
      <td><strong>6. Ay</strong></td>
      <td>Bağımsız test serilerinde nihai karşılaştırmalı değerlendirmenin yapılması, açık kaynak kod havuzunun belgelenmesi ve teknik proje sonuçlarının derlenmesi</td>
      <td>Burak ERDOĞAN (Danışman gözetiminde)</td>
      <td>Bağımsız test grubunda adil kıyaslama analizlerinin tamamlanması, açık erişimli kod deposunun belgelenmesi ve teknik sonuçların raporlanması (%10)</td>
    </tr>
  </table>
</div>

<!-- ALAN 7: 3.2 RİSK YÖNETİMİ -->
<div class="section-card">
  <div class="section-title">
    <span>7. 3.2. RİSK YÖNETİMİ</span>
    <span class="tybs-tag">TYBS: Risk Yönetimi Ekranı</span>
  </div>
  <table>
    <tr>
      <th style="width: 45%;">En Önemli Riskler</th>
      <th style="width: 55%;">Alınacak Tedbirler (B Planı)</th>
    </tr>
    <tr>
      <td>Gerçek süreç anomalisinin sensör hatası sanılarak bastırılması ve kritik bir makine arızasının kaçırılması riski.</td>
      <td>Süreç karar katmanında yalnızca tek bir sensöre güvenilmeyecek; diğer fiziksel sensörlerde eşzamanlı sapma görüldüğünde süreç alarmına öncelik veren güvenlik ağırlıklı hiyerarşik karar kuralı uygulanacaktır.</td>
    </tr>
    <tr>
      <td>Referans olarak kabul edilen ikinci sensörün de bozulması veya çoklu sensör arızası yaşanması durumunda tutarlılık modelinin yanılması.</td>
      <td>İkili ilişkiler yerine çok değişkenli artık analizi izlenecek; sensörler arası tutarsızlık geneli kapsadığında veya veri yetersiz kaldığında sistem zorla normal kararı vermeyip 'Değerlendirilemiyor' bayrağı kaldıracaktır.</td>
    </tr>
    <tr>
      <td>Sensörler arası ilişkinin doğrusal olmaması veya çalışma rejimine göre değişmesi sebebiyle doğrusal artık modelinin hatalı alarm üretmesi.</td>
      <td>Doğrusal regresyona ek olarak çekirdekli PCA (Kernel PCA) ve yerel k-en yakın komşu gibi doğrusal olmayan alternatifler doğrulama verisinde karşılaştırılacak ve en kararlı yapı seçilecektir.</td>
    </tr>
    <tr>
      <td>Veri setinde yer alan 2 saniyenin üzerindeki zaman atlamalarının zaman serisi modellerinin pencereleme düzenini bozması.</td>
      <td>Zaman boşlukları yapay verilerle doldurulmayacak; atlama süresi nominal periyodun 3 katını aştığında zaman penceresi sıfırlanacak ve boşluk süresince durum belirsiz olarak etiketlenecektir.</td>
    </tr>
  </table>
</div>

<div class="page-break"></div>

<!-- ALAN 8: 3.3 ARAŞTIRMA OLANAKLARI -->
<div class="section-card">
  <div class="section-title">
    <span>8. 3.3. ARAŞTIRMA OLANAKLARI</span>
    <span class="tybs-tag">TYBS: Araştırma Olanakları Ekranı</span>
  </div>
  <p class="note">Not: Marka ve donanım üretici isimleri ön eleme riskine karşı akademik olarak anonimleştirilmiştir.</p>
  <table>
    <tr>
      <th style="width: 45%;">Kuruluşta Bulunan Altyapı / Ekipman Türü</th>
      <th style="width: 55%;">Projede Kullanım Amacı</th>
    </tr>
    <tr>
      <td><strong>Kişisel Bilgisayar Geliştirme Ortamı</strong> (Çok çekirdekli işlemci, 16 GB sistem belleği, yerel yüksek hızlı depolama)</td>
      <td>Veri hazırlama betiklerinin koşturulması, sentetik bozulma simülasyonları, makine öğrenmesi modellerinin eğitimi, test koşuları ve grafiksel analizler.</td>
    </tr>
    <tr>
      <td><strong>Açık Kaynaklı Veri ve Yazılım Altyapısı</strong> (SKAB Kıyaslama Veri Kümesi, açık kaynaklı bilimsel hesaplama ve makine öğrenmesi kütüphaneleri, sürüm kontrollü kod deposu)</td>
      <td>Çok değişkenli zaman serisi analizi, doğrusal ve çekirdekli modellerin kodlanması, sürüm kontrolü ve tekrarlanabilir deney arşivinin tutulması.</td>
    </tr>
    <tr>
      <td><strong>Üniversite Kütüphanesi ve Akademik Veri Tabanı Ağları</strong> (Ulusal ve uluslararası hakemli akademik veri tabanları ile elektronik kütüphane erişim ağları)</td>
      <td>Endüstriyel anomali tespiti, sensör güvenilirliği ve kestirimci bakım literatüründeki güncel makale ve konferans bildirilerinin temini.</td>
    </tr>
  </table>
</div>

<!-- ALAN 9: 4. YAYGIN ETKİ -->
<div class="section-card">
  <div class="section-title">
    <span>9. 4. YAYGIN ETKİ</span>
    <span class="tybs-tag">TYBS: Yaygın Etki Ekranı</span>
  </div>
  <table>
    <tr>
      <th style="width: 30%;">Çıktı, Etki ve Kazanımlar</th>
      <th style="width: 70%;">Öngörülen Çıktı(lar), Etki(ler) ve Kazanım(lar)</th>
    </tr>
    <tr>
      <td><strong>Bilimsel / Akademik Çıktılar</strong><br><small>(Makale, Bildiri vb.)</small></td>
      <td>Araştırma bulguları, endüstriyel veri kalitesi ve anomali tespiti alanında ulusal veya uluslararası düzeyde hakemli bir mühendislik konferansına bildiri olarak sunulmak üzere hazırlanacaktır. Deney protokolü, veri bölme kayıt dosyaları ve geliştirilen kaynak kodlar açık erişimli ve sürüm kontrollü bir kod deposunda yayımlanarak araştırmacıların ve lisans öğrencilerinin erişimine açılacaktır.</td>
    </tr>
    <tr>
      <td><strong>Ekonomik / Ticari Çıktılar</strong><br><small>(Ürün, Karar Destek vb.)</small></td>
      <td>Önerilen yaklaşım, kestirimci bakım yazılımlarında hatalı sensör ölçümlerinden kaynaklanan gereksiz süreç alarmlarını azaltarak bakım ekiplerinin karar güvenilirliğini destekleme potansiyeli taşımaktadır. İleride endüstriyel IoT izleme sistemlerine entegre edilebilecek hafif ve yorumlanabilir bir karar destek mantığı ortaya konulacaktır.</td>
    </tr>
    <tr>
      <td><strong>Yeni Projeler Oluşturma</strong><br><small>(Yarışma, Lisansüstü vb.)</small></td>
      <td>Bu projede kurulacak sentetik bozulma ve ayrık değerlendirme altyapısı, ilerleyen aşamalarda sanayiye yönelik lisans araştırma projeleri veya ulusal teknoloji ve inovasyon yarışmalarına sunulacak gerçek zamanlı gömülü kestirimci bakım prototipleri için temel teşkil edecektir.</td>
    </tr>
  </table>
</div>

<!-- ALAN 10: 5. DİĞER KONULAR -->
<div class="section-card">
  <div class="section-title">
    <span>10. 5. BELİRTMEK İSTEDİĞİNİZ DİĞER KONULAR</span>
    <span class="tybs-tag">TYBS: Diğer Konular Ekranı</span>
  </div>
  <div class="copy-text">SKAB 'other/5' (rotor dengesizliği) deneyi üzerinde kural tabanlı bir başlangıç demosu gerçekleştirilmiştir. Birinci ivmeölçerin 120–319 örnek indekslerine (başlangıçtan itibaren 126–336. saniyeler arasına) doğrusal olarak 0–0,35 g kayma eklenmiştir. Bu bölgedeki 200 örneğin 191'inde temel yöntem süreç alarmı üretirken, ikinci ivmeölçerden süreç kanıtı arayan kural tabanlı başlangıç yaklaşımı aynı bölgede süreç alarmı üretmemiştir. Her iki yaklaşım, kaynak etiketi anomalili olan 410 örneğin tamamında (600–1.028. saniyeler arası) alarm üretmiştir. Bulgular tek deney ve tek bozulma senaryosuyla sınırlı olup, bağımsız test gruplarına genellenebilirlik proje kapsamında araştırılacaktır. İlgili karşılaştırma grafiği results/demo/pilot_demo_karsilastirma.png dosyasında arşivlenmiştir.

Araştırma kapsamında yararlanılan akademik kaynaklar metin içi atıflarla eşleştirilerek EK-1 Kaynaklar bölümünde listelenmiştir. Çalışmada açık kaynaklı laboratuvar verileri kullanılacağından insan veya hayvan katılımcı içermemekte olup, etik kurul onay belgesi veya özel izin gerektiren bir ek bulunmamaktadır.</div>
</div>

<div class="page-break"></div>

<!-- ALAN 11: 6. BÜTÇE KALEMLERİ VE GEREKÇELERİ -->
<div class="section-card">
  <div class="section-title">
    <span>11. BÜTÇE KALEMLERİ VE GEREKÇELERİ (ÖNEMLİ VE REVİZE EDİLMİŞ)</span>
    <span class="tybs-tag">TYBS: Bütçe / Harcama Kalemleri Ekranı</span>
  </div>
  <p class="note">Not: "137 GB boş alan var" çelişkisi kaldırılmış; Colab Pro+ yerine genel bulut hesaplama ve demirbaş devir şartı eklenmiştir.</p>
  
  <div style="margin-bottom: 12px;">
    <strong>1. Makine ve Teçhizat Gideri: Harici Taşınabilir SSD (500 GB, Yüksek Hızlı Bağlantı) - 5.000 TL</strong>
    <div class="copy-text">Proje süresince 35 bağımsız deney serisine uygulanacak sentetik bozulma permütasyonları (4 bozulma türü x 5 şiddet seviyesi x 10 tekrarlı tohum koşuları), ara model ağırlıkları, matris çıktıları ve detaylı deney kayıtlarının (log) ana çalışma bilgisayarından bağımsız, veri kaybını önleyici harici güvenli bir yedekleme biriminde arşivlenmesi planlanmaktadır. Alınacak harici depolama birimi demirbaş niteliğinde olup, proje tamamlandığında kurum/bölüm araştırma laboratuvarı envanterine devredilecektir. Bu gider için 5.000 TL talep edilmektedir.</div>
  </div>

  <div style="margin-bottom: 12px;">
    <strong>2. Hizmet Alımı Gideri: Altı Aylık Bulut Tabanlı Yüksek Bellekli Hesaplama Hizmeti - 4.961 TL</strong>
    <div class="copy-text">Projenin altı aylık çalışma süresince, 35 veri dosyasında 10 farklı rastgele tohumla yürütülecek Monte Carlo deneylerinin, çok değişkenli artık analizlerinin, çekirdekli doğrusal olmayan model optimizasyonlarının ve parametrik şiddet taramalarının yerel geliştirme bilgisayarını kilitlemeden, arka planda uzun süreli toplu iş parçacıklarıyla (batch processing) kesintisiz koşturulabilmesi amacıyla bulut tabanlı yüksek bellekli hesaplama hizmeti kullanımı planlanmaktadır. Yüksek bellekli sanal makine altyapısı, çoklu bozulma senaryolarının eşzamanlı çalıştırılmasını sağlayacaktır. İlgili bulut hizmetinin aylık abonelik bedeli vergiler dahil 826,80 TL olup, altı aylık toplam tutar 4.960,80 TL olarak hesaplanmıştır. Başvuru sistemine tam sayı girildiğinden 4.961 TL talep edilmektedir.</div>
  </div>

  <div>
    <strong>3. Diğer Giderler & Toplam Destek Tutarı:</strong>
    <div class="copy-text">Sarf malzemesi ve ulaşım giderleri için destek talep edilmemektedir.

TOPLAM TALEP EDİLEN DESTEK TUTARI: 9.961 TL (Limit olan 12.000 TL dahilindedir)</div>
  </div>
</div>

<!-- ALAN 12: EK-1: KAYNAKLAR -->
<div class="section-card">
  <div class="section-title">
    <span>12. EK-1: KAYNAKLAR (TAM VE DOĞRULANMIŞ 10 KAYNAK)</span>
    <span class="tybs-tag">TYBS: Kaynaklar Ekranı</span>
  </div>
  <div class="copy-text">1. Katser, I. D., & Kozitsin, V. O. (2020). Skoltech Anomaly Benchmark (SKAB). Kaggle. https://doi.org/10.34740/KAGGLE/DSV/1693952
2. Türkdamar, M. U., & Öztürk, C. (2025). Anomaly Detection on Industrial Processes with Convolutional Neural Networks. International Cumhuriyet Artificial Intelligence Conference (CAIAC 2025) Bildiriler Kitabı, Sivas, 29.
3. Sun, D., Fan, Y., & Wang, G. (2024). Enhancing Fault Diagnosis in Industrial Processes through Adversarial Task Augmented Sequential Meta-Learning. Applied Sciences, 14(11), 4433. https://doi.org/10.3390/app14114433
4. Teng, S., & Gao, X. (2026). Causal Wavelet Residual Learning with Observation-Support Gating for Industrial Sensor Anomaly Detection. Sensors, 26(18), 5751. https://doi.org/10.3390/s26185751
5. Zhang, J., Luo, W., & Dai, Y. (2021). Integrated Diagnostic Framework for Process and Sensor Faults in Chemical Industry. Sensors, 21(3), 822. https://doi.org/10.3390/s21030822
6. Liu, F. T., Ting, K. M., & Zhou, Z. H. (2008). Isolation Forest. 2008 Eighth IEEE International Conference on Data Mining, 413–422. https://doi.org/10.1109/ICDM.2008.17
7. Mahalanobis, P. C. (1936). On the generalized distance in statistics. Proceedings of the National Institute of Sciences of India, 2(1), 49–55.
8. Dunia, R., & Qin, S. J. (1996). Subspace approach to multidimensional fault identification and reconstruction. AIChE Journal, 42(8), 2308–2320. https://doi.org/10.1002/aic.690420816
9. T.C. Cumhurbaşkanlığı Strateji ve Bütçe Başkanlığı. (2023). On İkinci Kalkınma Planı (2024–2028). Ankara.
10. T.C. Sanayi ve Teknoloji Bakanlığı. (2025). 2030 Sanayi ve Teknoloji Stratejisi. Ankara.</div>
</div>

<div class="alert-box" style="margin-top: 20px;">
  <strong>📌 BELGE YÜKLEME (EK) HATIRLATMASI:</strong><br>
  TYBS'ye metinleri girdikten sonra, "Araştırma Önerisi Formu" yükleme alanına projenin Word çıktısı olan <code>rapor_ornekleri/2209-A_arastirma_onerisi_formu_DOLDURULMUS.docx</code> dosyasından üretilen temiz PDF'i yükleyiniz. Word'den PDF alırken "Yazı tiplerini katıştır (Embed fonts)" veya "PDF/A" seçeneğinin açık olduğundan emin olunuz; böylece Türkçe karakterler (ğ, ş, ı, İ) asla silinmeyecektir.
</div>

</body>
</html>
"""

with open("docs/tybs_rehber_sablon.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML şablonu oluşturuldu, şimdi Playwright ile PDF'e dönüştürülüyor...")

pdf_output_path = os.path.abspath("TUBITAK_2209A_TYBS_Guncellenecek_Metinler.pdf")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.set_content(html_content, wait_until="networkidle")
    page.pdf(
        path=pdf_output_path,
        format="A4",
        print_background=True,
        margin={"top": "14mm", "bottom": "14mm", "left": "14mm", "right": "14mm"}
    )
    browser.close()

print(f"PDF Başarıyla Üretildi: {pdf_output_path}")
print(f"PDF Boyutu: {os.path.getsize(pdf_output_path)} bayt")
