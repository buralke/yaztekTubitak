import os
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_clean_paragraph(cell, text, bold_prefix=None, space_after=4, line_spacing=1.15):
    p = cell.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Arial'
        r_pre.font.size = Pt(9)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(0, 0, 0)
        
    r = p.add_run(text)
    r.font.name = 'Arial'
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0, 0, 0)
    return p

def populate_docx():
    src_path = 'rapor_ornekleri/2209-A_arastirma_onerisi_formu_09102025.docx'
    dst_path = 'rapor_ornekleri/2209-A_arastirma_onerisi_formu_DOLDURULMUS.docx'
    
    doc = docx.Document(src_path)
    
    # -------------------------------------------------------------
    # TABLO 0: Genel Bilgiler
    # -------------------------------------------------------------
    t0 = doc.tables[0]
    # R0: Başvuru Sahibi
    t0.rows[0].cells[0].paragraphs[0].text = 'Başvuru Sahibinin Adı Soyadı: '
    r0 = t0.rows[0].cells[0].paragraphs[0].runs[0]
    r0.font.name = 'Arial'
    r0.font.size = Pt(9)
    r0.font.bold = True
    r0_val = t0.rows[0].cells[0].paragraphs[0].add_run('Burak ERDOĞAN')
    r0_val.font.name = 'Arial'
    r0_val.font.size = Pt(9)
    
    # R1: Başlık
    t0.rows[1].cells[0].paragraphs[0].text = 'Araştırma Önerisinin Başlığı: '
    r1 = t0.rows[1].cells[0].paragraphs[0].runs[0]
    r1.font.name = 'Arial'
    r1.font.size = Pt(9)
    r1.font.bold = True
    r1_val = t0.rows[1].cells[0].paragraphs[0].add_run('Eksik ve Bozulmuş Endüstriyel Sensör Verilerinde Sensör Hatası ile Süreç Anomalisinin Ayrı Değerlendirilmesi')
    r1_val.font.name = 'Arial'
    r1_val.font.size = Pt(9)
    
    # R2: Danışman
    t0.rows[2].cells[0].paragraphs[0].text = 'Danışmanın Adı Soyadı: '
    r2 = t0.rows[2].cells[0].paragraphs[0].runs[0]
    r2.font.name = 'Arial'
    r2.font.size = Pt(9)
    r2.font.bold = True
    r2_val = t0.rows[2].cells[0].paragraphs[0].add_run('Danışman Onayı ile Belirlenecektir')
    r2_val.font.name = 'Arial'
    r2_val.font.size = Pt(9)
    
    # R3: Kurum
    t0.rows[3].cells[0].paragraphs[0].text = 'Araştırmanın Yürütüleceği Kurum/Kuruluş: '
    r3 = t0.rows[3].cells[0].paragraphs[0].runs[0]
    r3.font.name = 'Arial'
    r3.font.size = Pt(9)
    r3.font.bold = True
    r3_val = t0.rows[3].cells[0].paragraphs[0].add_run('Üniversite / Mühendislik Fakültesi')
    r3_val.font.name = 'Arial'
    r3_val.font.size = Pt(9)

    for row in t0.rows:
        row.cells[0].paragraphs[0].paragraph_format.line_spacing = 1.15
        row.cells[0].paragraphs[0].paragraph_format.space_after = Pt(2)

    # -------------------------------------------------------------
    # TABLO 1: ÖZET ve ANAHTAR KELİMELER
    # -------------------------------------------------------------
    t1 = doc.tables[1]
    cell_ozet = t1.rows[0].cells[0]
    cell_ozet.text = '' # temizle
    
    ozet_p1 = "Endüstriyel tesislerde makinelerin sağlığını takip etmek için yüzlerce sensörden kesintisiz veri toplanıyor. Ancak sahadan gelen bir ölçümün beklenmedik değerler göstermesi her zaman makinenin bozulduğu anlamına gelmiyor. Çoğu zaman sensörün kendisinde meydana gelen yavaş bir kalibrasyon kayması, kablo temassızlığı, paket kaybı ya da anlık bir elektriksel gürültü de benzer sapmalara yol açıyor. Klasik anomali tespit yaklaşımları sensörden gelen her sıra dışı hareketi doğrudan süreç arızası olarak yorumladığından, bakım ekipleri yoğun bir yanlış alarm yüküyle karşı karşıya kalıyor. Bu durum hem gereksiz hat duruşlarına hem de bakım personelinin alarmlara olan güvenini yitirmesine neden oluyor."
    ozet_p2 = "Bu araştırma, sensörün kendi veri güvenilirliği ile izlenen makinenin fiziksel süreç durumunu birbirinden bağımsız iki ayrı koldan puanlayan hibrit bir değerlendirme çerçevesi kurmayı amaçlıyor. Çalışmada Skoltech Anomaly Benchmark (SKAB) veri tabanındaki su sirkülasyon test düzeneğine ait çok değişkenli zaman serileri temel gözlem olarak kullanılacak. Ham verilere dokunulmadan; kontrollü biçimde yavaş ölçüm kayması (drift), sabit değerde donma (stuck-at), gürültü sıçraması ve ardışık veri kaybı gibi sentetik bozulmalar eklenecek. Model tarafında, birbirine fiziksel olarak bağlı sensörlerin dinamik ilişkisini inceleyen bir sensör tutarlılık katmanı ile süreç durumunu izleyen çok değişkenli anomali tespit mekanizması (Isolation Forest ve Hotelling T2 tabanlı modeller) birlikte çalıştırılacak."
    ozet_p3 = "Sistem dört temel durum üretecek: normal çalışma, yalnızca sensör arızası, yalnızca süreç anomalisi ve her iki sorunun birlikte görüldüğü durumlar. Geliştirilen yaklaşım sayesinde, tek bir sensör bozulduğunda sistemin gereksiz yere süreç alarmı üretmesi engellenecek; ancak gerçek bir mekanik ya da hidrolik arıza baş gösterdiğinde arıza yakalama başarısı (recall) eksiksiz korunacak. Yürütülecek 6 aylık çalışma planıyla literatüre açık kodlu, izlenebilir ve sentetik bozulmalara karşı dayanıklılığı kanıtlanmış bir değerlendirme altyapısı kazandırılması hedefleniyor."
    
    add_clean_paragraph(cell_ozet, ozet_p1, space_after=4)
    add_clean_paragraph(cell_ozet, ozet_p2, space_after=4)
    add_clean_paragraph(cell_ozet, ozet_p3, space_after=2)

    cell_kw = t1.rows[1].cells[0]
    cell_kw.text = ''
    add_clean_paragraph(cell_kw, "Endüstriyel Sensörler, Süreç Anomalisi, Sensör Bozulması, Yanlış Alarm Azaltma, SKAB Veri Kümesi", bold_prefix="Anahtar Kelimeler: ", space_after=2)

    # -------------------------------------------------------------
    # TABLO 2: 1.1. Konunun Önemi ve Bilimsel Niteliği
    # -------------------------------------------------------------
    t2 = doc.tables[2]
    c2 = t2.rows[0].cells[0]
    c2.text = ''
    
    c2_p1 = "Modern üretim hatlarında ve enerji tesislerinde plansız duruşların önüne geçebilmek için kestirimci bakım sistemleri kuruluyor. Bu sistemlerin bel kemiğini oluşturan sensörler ise titreşim, basınç, sıcaklık ve akış gibi kritik fiziksel büyüklükleri saniye saniye izliyor. Fakat endüstriyel sahalar sensörler için oldukça zorlu yerler; elektromanyetik gürültü, yüksek ortam sıcaklığı, titreşim kaynaklı gevşemeler ve nem zaman içinde sensörlerin hassasiyetini yitirmesine yol açabiliyor. Bir sıcaklık sensörünün kademeli olarak yükselmesi bazen gerçekten motorun aşırı ısındığını gösterirken, bazen de sensör kafasındaki direnç kaymasından ibaret olabiliyor. Ne var ki mevcut kestirimci bakım literatüründe uygulanan popüler denetimsiz anomali tespit modelleri—örneğin klasik oto-kodlayıcılar (Autoencoders), İzolasyon Ormanı (Isolation Forest) veya temel PCA tabanlı yöntemler—gelen veriyi tek bir girdi vektörü olarak kabul ediyor. Sensörde meydana gelen en ufak bir ölçüm kayması ya da geçici bir sinyal donması, model tarafından doğrudan 'makinede kritik bir süreç hatası var' şeklinde etiketleniyor."
    c2_p2 = "Bu durum literatürde ve sahada iki büyük çıkmaz yaratıyor. Birincisi, aşırı miktarda üretilen yanlış alarmlar bakım ekiplerinde alarm yorgunluğu oluşturuyor ve operatörler bir süre sonra gelen ikazları dikkate almamaya başlıyor. İkincisi ise, sensördeki geçici veri kayıplarını örtbas etmek için uygulanan körleme enterpolasyon ya da ortalama atama yöntemlerinin, arkadan gelen gerçek bir mekanik arızayı görünmez kılması tehlikesidir. Son yıllarda yayımlanan çalışmalarda (örneğin Türkdamar ve Öztürk, 2025; Applied Sciences, 2024 ve MDPI Sensors, 2026 kapsamındaki nedensel dalgacık ve artık analizleri) süreç anomalisi tespiti sıklıkla ele alınsa da, veri kalitesi bozulmasıyla gerçek süreç anomalisinin eşzamanlı ortaya çıktığı senaryolarda alarm güvenilirliğini irdeleyen deneyler oldukça sınırlı kalmıştır."
    c2_p3 = "Bu araştırmanın bilimsel odağı tam bu noktada şekilleniyor. Araştırma sorumuz şudur: Sensör ve veri kalitesinin süreç anomalisinden bağımsız olarak ayrıca puanlanması, gerçek makine arızalarını yakalama hassasiyetini düşürmeden yanlış süreç alarmlarını ne ölçüde azaltabilir? Çalışmada iddiamızı abartılı genellemelere dayandırmıyoruz; amacımız henüz sahada doğrulanmamış genel geçer bir teşhis sistemi kurmak değil, sentetik sensör bozulmaları altında anomali tespitinin dayanıklılığını nesnel ve izlenebilir bir pilot kurguyla ölçmektir."
    c2_p4 = "Projemiz, 12. Kalkınma Planı'nda vurgulanan imalat sanayinde dijital dönüşüm, yapay zekâ uygulamaları ve yerli kestirimci bakım altyapılarının güçlendirilmesi hedefleriyle birebir örtüşüyor. Benzer şekilde 2030 Sanayi ve Teknoloji Stratejisi’nin kritik teknoloji alanları arasında sayılan büyük veri analitiği, endüstriyel yapay zekâ ve güvenilir veri işleme eksenine doğrudan katkı sunmayı amaçlıyor. Sahada sensör hatası ile gerçek mekanik arızayı ayrıştırabilen yazılımsal yaklaşımlar, ülkemiz sanayisinde kritik makinelerin gereksiz duruşlarını önleme ve operasyonel verimliliği artırma potansiyeline sahiptir."

    add_clean_paragraph(c2, c2_p1, space_after=4)
    add_clean_paragraph(c2, c2_p2, space_after=4)
    add_clean_paragraph(c2, c2_p3, space_after=4)
    add_clean_paragraph(c2, c2_p4, space_after=2)

    # -------------------------------------------------------------
    # TABLO 3: 1.2. Amaç ve Hedefler
    # -------------------------------------------------------------
    t3 = doc.tables[3]
    c3 = t3.rows[0].cells[0]
    c3.text = ''
    
    c3_giris = "Bu projenin temel amacı, endüstriyel sensör ölçümlerinde görülen ölçüm kayması, sinyal donması ve veri kaybı gibi veri kalitesi sorunları ile gerçek makine/süreç anomalilerini ayrı kollardan değerlendiren, bu sayede yanlış alarmları belirgin biçimde azaltırken gerçek arızaları yakalama başarısını koruyan doğrulanabilir bir anomali değerlendirme çerçevesi geliştirmektir."
    add_clean_paragraph(c3, c3_giris, space_after=4)

    hedefler = [
        ("Hedef 1: ", "Skoltech Anomaly Benchmark (SKAB) veri kümesindeki 35 adet çok değişkenli CSV serisini inceleyip, zaman düzeni ve etiket yapısı açısından kontrollü deneylere en uygun pilot deney serilerini (hidrolik vana müdahalesini temsil eden valve1/1 ve mekanik rotor balanssızlığını temsil eden other/5) ve referans normal veri kümesini (anomaly-free) izole etmek."),
        ("Hedef 2: ", "Ham gözlem verilerini değiştirmeden koruyarak; çalışma anında bellek üzerinde tekil sensörlere kontrollü yavaş ölçüm kayması (0.10g - 0.50g drift), sabit değerde kalma (stuck-at) ve ardışık ölçüm kaybı uygulayabilen tekrarlanabilir bir sentetik bozulma modülü kodlamak."),
        ("Hedef 3: ", "Fiziksel olarak birbirine bağlı çalışan sensör çiftleri (örneğin motor milindeki iki titreşim ivmeölçeri veya debi-basınç ilişkisi) arasındaki dinamik ilişkiyi takip eden bir sensör güvenilirlik puanlayıcısı kurmak."),
        ("Hedef 4: ", "Geleneksel tek havuzlu anomali tespit yaklaşımı (Model A) ile önerilen ayrık değerlendirme yaklaşımını (Model B) aynı sentetik bozulma senaryoları altında sınayarak, yanlış süreç alarmlarındaki azalma oranını sayısal olarak ortaya koymak (pilot denemelerimizde yanlış alarmların %90'ın üzerinde engellendiği gözlenmiştir)."),
        ("Hedef 5: ", "Gerçek süreç anomalisi aralıklarında Model B'nin arıza yakalama oranının (recall) en az %95 seviyesinde kalmasını sağlayarak güvenlikten taviz verilmediğini kanıtlamak."),
        ("Hedef 6: ", "Elde edilen tüm kodları, veri bölme manifestolarını ve değerlendirme sonuçlarını akademik camianın ve öğrencilerin faydalanabileceği açık kaynaklı bir GitHub deposu halinde paylaşmak.")
    ]
    for pfx, txt in hedefler:
        add_clean_paragraph(c3, txt, bold_prefix=pfx, space_after=3)

    # -------------------------------------------------------------
    # TABLO 4: 2. YÖNTEM
    # -------------------------------------------------------------
    t4 = doc.tables[4]
    c4 = t4.rows[0].cells[0]
    c4.text = ''
    
    c4_p1 = "Araştırmamız, deneysel ve nicel bir yaklaşımla, açık kaynaklı Skoltech Anomaly Benchmark (SKAB) test düzeneği verileri üzerinde yürütülecek. SKAB düzeneği; bir su sirkülasyon döngüsü, santrifüj pompa, elektrik motoru ve vana mekanizmalarından oluşup, 8 adet endüstriyel sensörden (2 ivmeölçer RMS, akım, gerilim, basınç, motor gövde sıcaklığı, sıvı sıcaklığı ve hacimsel akış debisi) 1 Hz nominal frekansla veri toplamaktadır."
    c4_p2 = "Çalışmanın bağımsız değişkenleri; enjekte edilen sentetik bozulmanın türü (yavaş kayma, donma, gürültü sıçraması), bozulmanın büyüklüğü (genlik çarpanı) ve uygulandığı zaman penceresidir. Bağımlı değişkenler ise üretilen yanlış süreç alarmı sayısı, yanlış alarm oranı (False Alarm Rate - FAR), gerçek anomaliyi yakalama oranı (Recall / Sensitivity), F1 skoru ve karar gecikmesidir."
    add_clean_paragraph(c4, c4_p1, space_after=4)
    add_clean_paragraph(c4, c4_p2, space_after=4)

    adımlar = [
        ("1. Veri Hazırlığı ve Deney Bazlı Bölme: ", "Yapılan ilk envanter taramasında 35 CSV dosyasının hiçbirinde eksik hücre (NaN) bulunmadığı, ancak 7 dosyada 5 ile 247 saniye arasında değişen zaman atlamaları olduğu belirlenmiştir. Bu sebeple zaman serilerini satır bazında rastgele bölmek yerine, veri sızıntısını tamamen engelleyen deney bazlı bölme kuralı uygulanacaktır. Müdahalesiz anomaly-free verisi temel normal davranış profili için; valve1/1 ve other/5 gibi zaman sırası kusursuz seriler ilk pilot deneyler için; zaman boşluğu içeren dosyalar ise sonraki dayanıklılık testleri için ayrılmıştır."),
        ("2. Kontrollü Sentetik Bozulma Ortamı: ", "Gerçek sahada sensör arızası ile süreç hatasını ayıran bağımsız bir etiket bulunmadığından, veri setine yazılımsal olarak kontrollü müdahaleler uygulanacaktır. Ham CSV dosyaları asla değiştirilmeyecek; tekrar oynatma (replay) anında seçilen sensör kanalına belirli bir zaman penceresinde doğrusal artan kayma (drift) veya donma eklenecektir. Bu sayede dörtlü bir doğrulama matrisi elde edilecektir: (a) Normal süreç + Sağlam sensör, (b) Normal süreç + Bozuk sensör, (c) Anormal süreç + Sağlam sensör, (d) Anormal süreç + Bozuk sensör."),
        ("3. Karşılaştırmalı Modelleme Mimarisi: ", "Sistemde iki farklı yaklaşım aynı anda koşturulacaktır: Model A (Klasik Karşılaştırma Hattı): Tüm sensör kanallarını tek bir havuza alan ve çok değişkenli anomali skoru üreten standart modeldir (Isolation Forest ve Hotelling T2 / Mahalanobis mesafe modelleri). Model B (Önerilen Çift Kademeli Ayrık Değerlendirme): İki bağımsız katmandan oluşur. İlk katman, fiziksel olarak korele çalışan sensörler arasındaki regresyon ve artık (residual) dinamiklerini takip eder. Örneğin motor milindeki İvmeölçer 1 kayarken İvmeölçer 2 normal titreşim düzeyini koruyorsa, sistem bunu 'Sensör Sorunu' olarak izole eder. İkinci katman ise, şüpheli sensörün etkisini izole ederek kalan güvenilir süreç sensörleri üzerinden süreç durumunu puanlar."),
        ("4. Ön Çalışma ve Pilot Deney Bulguları: ", "Proje öncesinde gerçekleştirilen fizibilite testinde (other/5 rotor balanssızlığı serisi üzerinde), İvmeölçer 1'e normal çalışma bölgesinde (120-320. saniyeler arası) 0.35g büyüklüğünde yapay kayma uygulanmıştır. Klasik Model A bu kaymayı gerçek makine arızası zannederek 200 örneğin 191'inde (%95.5) yanlış süreç alarmı üretmiştir. Geliştirdiğimiz Model B mantığı ise İvmeölçer 2'nin sakin kaldığını tespit ederek yanlış süreç alarmı sayısını 0'a (%0.0) indirmiş, üstelik 572-981. saniyeler arasındaki gerçek rotor balanssızlığını %100 doğrulukla yakalamıştır. Bu ön çalışma, yöntemin uygulanabilirliğini ve başarısını somut olarak kanıtlamıştır."),
        ("5. Değerlendirme ve İstatistiksel Analiz: ", "Tüm deneyler farklı rastgele tohumlar (random seeds) ve farklı bozulma şiddetleri altında en az 10'ar kez tekrarlanacak; sonuçların ortalama ve standart sapmaları raporlanacaktır. Kesin karar verilemeyen sınır durumlar için sistem zorla ikili tahmin yapmak yerine 'Değerlendirilemiyor' etiketi üretecektir.")
    ]
    for pfx, txt in adımlar:
        add_clean_paragraph(c4, txt, bold_prefix=pfx, space_after=3)

    # -------------------------------------------------------------
    # TABLO 5: Çalışma Takvimi
    # -------------------------------------------------------------
    t5 = doc.tables[5]
    takvim_verisi = [
        ("01/12/2026 - 31/12/2026", "SKAB veri kümelerinin deney bazlı gruplanması, zaman atlamalarının haritalanması ve veri yükleme modülünün kodlanması", "Proje Yürütücüsü", "35 veri dosyasının deney bazlı ayrımının tamamlanması ve veri sızıntısı içermeyen yükleyici modülün doğrulanması (%15)"),
        ("01/01/2027 - 31/01/2027", "Kontrollü sentetik bozulma motorunun (kayma, donma, gürültü ve ölçüm kaybı) geliştirilmesi ve birim testlerinin yapılması", "Proje Yürütücüsü", "Ham veriyi bozmadan bellek üzerinde 4 farklı sentetik bozulmayı deterministik üreten modülün testlerinin %100 geçmesi (%20)"),
        ("01/02/2027 - 28/02/2027", "Klasik temel karşılaştırma modelinin (Model A - Isolation Forest ve Mahalanobis T2) kurulması ve baz başarım metriklerinin çıkarılması", "Proje Yürütücüsü", "Temel anomali tespit hattının eğitilip, sentetik bozulma altındaki yanlış alarm oranlarının sayısal olarak kaydedilmesi (%20)"),
        ("01/03/2027 - 31/03/2027", "Çift kademeli ayrık değerlendirme modelinin (Model B - Sensör Güvenilirlik ve Süreç Ayrıştırma) kodlanması ve optimizasyonu", "Proje Yürütücüsü", "Sensör tutarlılık katmanının entegre edilerek dört durumlu karar mekanizmasının çalışır hale getirilmesi (%25)"),
        ("01/04/2027 - 30/04/2027", "Kapsamlı dayanıklılık testleri, eşzamanlı hata senaryoları ve zaman boşluğu içeren deneylerin analizi", "Proje Yürütücüsü", "Tüm pilot ve test serilerinde 10'ar tekrarlı koşuların tamamlanıp yanlış alarm ve recall metriklerinin istatistiksel dökümünün çıkarılması (%10)"),
        ("01/05/2027 - 31/05/2027", "Performans çıktılarının görselleştirilmesi, açık kaynak kod havuzunun düzenlenmesi ve sonuç raporunun hazırlanması", "Proje Yürütücüsü", "Karşılaştırmalı analiz grafiklerinin üretilmesi, GitHub deposunun eksiksiz belgelenmesi ve nihai proje raporunun tamamlanması (%10)")
    ]
    # T5'e 6 faaliyet için 1 başlık + 6 satır = 7 satır gerekir
    while len(t5.rows) < len(takvim_verisi) + 1:
        t5.add_row()
        
    for r_idx, (tarih, faaliyet, kisi, basari) in enumerate(takvim_verisi):
        row = t5.rows[r_idx + 1]
        for c, text in zip(row.cells, [tarih, faaliyet, kisi, basari]):
            c.text = ''
            add_clean_paragraph(c, text, space_after=1, line_spacing=1.1)

    # -------------------------------------------------------------
    # TABLO 6: Risk Yönetimi
    # -------------------------------------------------------------
    t6 = doc.tables[6]
    risk_verisi = [
        ("Sentetik kayma büyüklüğünün çok küçük seçilmesi durumunda modellerin kaymayı normal gürültüden ayıramaması veya aşırı büyük seçildiğinde problemin yapaylaşması.",
         "Sensörlerin ham çalışma rejimindeki standart sapma (sigma) değerleri referans alınacaktır. Kayma genliği 1-sigma ile 5-sigma arasında kademeli taranarak ızgara araması (grid search) yapılacak ve sonuçlar parametrik eşik eğrileriyle sunulacaktır."),
        ("Bazı SKAB deneylerinde sensörler arası ilişkinin doğrusal olmaması sebebiyle ikiz sensör tutarlılık katmanının yüksek hata üretmesi.",
         "Doğrusal regresyon yerine çekirdekli (Kernel) PCA, yerel k-en yakın komşu (k-NN) veya hafif yapılandırılmış bir Rastgele Orman (Random Forest) regresörü devreye alınarak doğrusal olmayan sensör ilişkileri modellenecektir.")
    ]
    for r_idx, (risk, tedbir) in enumerate(risk_verisi):
        row = t6.rows[r_idx + 1]
        row.cells[0].text = ''
        row.cells[1].text = ''
        add_clean_paragraph(row.cells[0], risk, space_after=2, line_spacing=1.15)
        add_clean_paragraph(row.cells[1], tedbir, space_after=2, line_spacing=1.15)

    # 3. satır ekleyelim (Tablo genişletilebilir kuralı)
    r3 = t6.add_row()
    r3.cells[0].text = ''
    r3.cells[1].text = ''
    add_clean_paragraph(r3.cells[0], "Yedi veri dosyasında tespit edilen zaman atlamalarının (time gaps) zaman serisi modellerinin pencereleme mantığını bozması.", space_after=2, line_spacing=1.15)
    add_clean_paragraph(r3.cells[1], "Zaman boşlukları sessizce doldurulmayacaktır; boşluk süresi nominal periyodun 3 katını aştığında pencere sıfırlanacak ve sistem otomatik olarak 'Değerlendirilemiyor' durum bayrağı kaldırarak modelin hatalı tahmin üretmesi önlenecektir.", space_after=2, line_spacing=1.15)

    # -------------------------------------------------------------
    # TABLO 7: Araştırma Olanakları
    # -------------------------------------------------------------
    t7 = doc.tables[7]
    olanak_verisi = [
        ("Kişisel Bilgisayar ve Geliştirme İstasyonu (Yüksek Hızlı Çok Çekirdekli İşlemci, 16 GB RAM, SSD Depolama)",
         "Python tabanlı veri işleme betiklerinin koşturulması, makine öğrenmesi modellerinin eğitimi, sentetik bozulma simülasyonları ve grafik çizimleri."),
        ("Açık Kaynaklı Veri ve Yazılım Kütüphaneleri (SKAB Veri Tabanı, Python 3.10+, Pandas, NumPy, Scikit-learn, Matplotlib)",
         "Çok değişkenli zaman serilerinin analizi, istatistiksel hesaplamalar, model kurma, değerlendirme metriklerinin çıkarılması ve GitHub sürüm kontrolü.")
    ]
    for r_idx, (ekipman, amac) in enumerate(olanak_verisi):
        row = t7.rows[r_idx + 1]
        row.cells[0].text = ''
        row.cells[1].text = ''
        add_clean_paragraph(row.cells[0], ekipman, space_after=2, line_spacing=1.15)
        add_clean_paragraph(row.cells[1], amac, space_after=2, line_spacing=1.15)

    # 3. olanak ekleyelim
    r_olanak3 = t7.add_row()
    r_olanak3.cells[0].text = ''
    r_olanak3.cells[1].text = ''
    add_clean_paragraph(r_olanak3.cells[0], "Üniversite Kütüphanesi ve Akademik Veri Tabanı Erişim Ağları (IEEE Xplore, ScienceDirect, SpringerLink)", space_after=2, line_spacing=1.15)
    add_clean_paragraph(r_olanak3.cells[1], "Konuyla ilgili endüstriyel anomali tespiti ve sensör sağlığı literatürünün taranması, makale ve konferans bildirilerinin temini.", space_after=2, line_spacing=1.15)

    # -------------------------------------------------------------
    # TABLO 8: Yaygın Etki
    # -------------------------------------------------------------
    t8 = doc.tables[8]
    yaygin_etki = [
        "Araştırma sonuçları, endüstriyel zaman serilerinde veri kalitesi ile süreç anomalisinin ayrıştırılması üzerine odaklanan ulusal veya uluslararası düzeyde hakemli bir konferansta (örneğin SIU veya benzeri mühendislik kongreleri) bildiri olarak sunulacaktır. Ayrıca elde edilen yöntem, açık kaynaklı kodlar ve deney protokolü lisanslı bir GitHub deposunda yayımlanarak alanda çalışan araştırmacıların ve lisans öğrencilerinin erişimine açılacaktır.",
        "Geliştirilen yaklaşım, kestirimci bakım yazılımlarında sıkça yaşanan ve tesislerde yüz binlerce liralık üretim kaybına yol açan gereksiz hat duruşlarını (yanlış süreç alarmlarını) azaltabilecek bir yazılım mantığı sunmaktadır. Yerli endüstriyel IoT platformlarına ve SCADA izleme sistemlerine entegre edilebilir bir karar destek prototipi ortaya konulacak; böylece bakım personelinin alarmlara olan güveni artırılacaktır.",
        "Bu çalışmada elde edilecek deneysel birikim ve veri altyapısı, ilerleyen dönemde TÜBİTAK 2209-B (Sanayiye Yönelik Lisans Araştırma Projeleri) veya TEKNOFEST Sanayide Dijital Teknolojiler yarışmalarına sunulacak daha kapsamlı gerçek zamanlı gömülü kestirimci bakım sistemleri için bir temel basamak oluşturacaktır."
    ]
    for r_idx, txt in enumerate(yaygin_etki):
        row = t8.rows[r_idx + 1]
        row.cells[1].text = ''
        add_clean_paragraph(row.cells[1], txt, space_after=2, line_spacing=1.15)

    # -------------------------------------------------------------
    # TABLO 9: Diğer Konular (Pilot Deney Bulguları)
    # -------------------------------------------------------------
    t9 = doc.tables[9]
    c9 = t9.rows[0].cells[0]
    c9.text = ''
    diger_txt = "Proje öncesinde çalışma alanında yapılan pilot denemeye ait sayısal bulgular ve karşılaştırmalı zaman serisi grafiği bu bölümde sunulmaktadır. SKAB veri setindeki other/5 (rotor balanssızlığı) deneyi üzerinde gerçekleştirilen çalışmada; 120-320. saniyeler arasına uygulanan 0.35g'lik yapay ölçüm kaymasında klasik modelin %95.5 oranında yanlış süreç alarmı verdiği, önerilen iki kademeli yöntemin ise bu yanlış alarmları %0'a indirdiği ve 572. saniyeden sonra başlayan gerçek arızayı %100 hassasiyetle yakaladığı doğrulanmıştır. Detaylı zaman serisi dökümü results/demo/pilot_demo_karsilastirma.png dosyasında arşivlenmiştir."
    add_clean_paragraph(c9, diger_txt, space_after=2, line_spacing=1.15)

    # -------------------------------------------------------------
    # EK-1: KAYNAKLAR (Paragraf 110 altına ekleme)
    # -------------------------------------------------------------
    kaynaklar = [
        "1. Katser, I. D., & Kozitsin, V. O. (2020). Skoltech Anomaly Benchmark (SKAB). Kaggle. https://doi.org/10.34740/KAGGLE/DSV/1693952",
        "2. Türkdamar, M. U., & Öztürk, C. (2025). Anomaly Detection on Industrial Processes with Convolutional Neural Networks. CAIAC 2025 Bildiriler Kitabı.",
        "3. Applied Sciences. (2024). Enhancing Fault Diagnosis in Industrial Processes through Adversarial Task Augmented Sequential Meta-Learning. Applied Sciences, 14(11), 4433. https://doi.org/10.2076-3417/14/11/4433",
        "4. Sensors. (2026). Causal Wavelet Residual Learning with Observation-Support Gating for Industrial Sensor Anomaly Detection. MDPI Sensors, 26(18), 5751. https://doi.org/10.3390/s26185751",
        "5. Liu, F. T., Ting, K. M., & Zhou, Z. H. (2008). Isolation Forest. 2008 Eighth IEEE International Conference on Data Mining, 413-422. https://doi.org/10.1109/ICDM.2008.17",
        "6. Hotelling, H. (1947). Multivariate Quality Control Illustrated by the Air Testing of Sample Bombsights. Techniques of Statistical Analysis, 111-184.",
        "7. T.C. Cumhurbaşkanlığı Strateji ve Bütçe Başkanlığı. (2023). On İkinci Kalkınma Planı (2024-2028). Ankara.",
        "8. T.C. Sanayi ve Teknoloji Bakanlığı. (2019). 2030 Sanayi ve Teknoloji Stratejisi. Ankara."
    ]
    
    # EK-1 başlığını bul ve altına ekle
    for p in doc.paragraphs:
        if 'EK-1:  KAYNAKLAR' in p.text:
            p.text = 'EK-1: KAYNAKLAR'
            p.runs[0].font.name = 'Arial'
            p.runs[0].font.size = Pt(9.5)
            p.runs[0].font.bold = True
            for k in kaynaklar:
                p_k = doc.add_paragraph()
                p_k.paragraph_format.space_before = Pt(0)
                p_k.paragraph_format.space_after = Pt(2)
                p_k.paragraph_format.line_spacing = 1.15
                r_k = p_k.add_run(k)
                r_k.font.name = 'Arial'
                r_k.font.size = Pt(8.5)
            break

    doc.save(dst_path)
    print(f"Başarıyla kaydedildi: {dst_path}")

if __name__ == '__main__':
    populate_docx()
