# Prepare-and-Send-Certificates
<h2>Uygulamanın Amacı ve Kullanımı</h2>
<p>Düzenlenen eğitimlerde katılımcılara sertfika gönderilmesi için tasarlanmış bir projedir. Python dili ile PIL, smtplib ve csv modülleri kullanılarak yazılmıştır.</p>

<p>Etkinliğe katılan katılımcıların isim-soyisim ve E-posta bilgilerini içeren google formu doldurması istenir. Etkinlik sonrası, bu formdaki bilgiler csv formatında alınır ve uygulamaya verilir. Bunun yanında sertifikanın boş şablonuda tasarlanır, isimlerin yazılacağı yazı fontu ve rengi belrlenir ve uygulamaya tanımlanır. </p>

<p>Uygulama, ilk aşamada listedeki isimler için birer sertifika hazırlar. İkinci aşamada ise, verilen onayla birlikte listedeki E-posta adreslerine ilgili sertifikaları gönderir. Bunun için, E-postaların gönderileceği mail adresi ve şifresi uygulama içinde tanımlı olmalıdır.</p>

<h2>Uygulamanın İmplementasyonu</h2>
<p>Proje Python dilinin OOP yapısı kullanılarak, iyi optimize edilmiş bir konsol uygulaması olarak geliştirilmiştir. Sınıf yapısında gerekli metotlar tanımlanmış. Main fonksiyonunda metotar çağrılarak uygulama gerçekleştirilmiştir. Bu metotlara bakacak olursak:</p>

<ol type="2">
  <li>__init__</li>
  <li>readCSV</li>
  <li>createCertificate</li>
  <li>prepareCertificates</li>
  <li>prepareMail</li>
  <li>sendMails</li>
</ol>

<p><b>__init__:</b>init fonksiyonu, uygulamanın gerekli argumanları aldığı metottur. Bütün yapılandırmaları bu metot üzerinde değiştirilebilir. </p>
<p><b>readCSV:</b> Alınan CSV dosyasını okuyup, anlamlı bir veriye dönüştüren metottur.</p>
<p><b>createCertificate:</b> Sertifika şablonunu ve üzerine yazılacak isim bilgisini alıp, sertifikayı hazırlayan metottur.</p>
<p><b>prepareCertificates:</b>sertifikaların kaydedileceği dizini oluşturan, readCSV metodundan gelen listeyi alıp, sırasıyla isimleri çeken ve createCertificate metoduna veren metottur.</p>
<p><b>prepareMail:</b> Sertifikanın gönderileceği E-posta ve png dosyasını alarak maili hazırlayan metottur.</p>
<p><b>sendMails:</b> İlgili smtp sunucusunu login olup, preparemail metodunun hazırlamış oldupu mailleri gönderen metottur.</p>

<p><b>__main__:</b> Uygulamadaki işlemlerin kontrol edildiği ana fonksiyondur.</p>








