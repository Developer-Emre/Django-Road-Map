## MODEL OLUŞTURMAK
Modeller classlardan oluşturulur ve modelsden bir miras alarak modelimiz oluşturulur. <br>

**models.py içerisinde oluşturulur** <br>

<img src="/04-MODELS/img/modelOrnegi.PNG"> <br> <br>

Yukarıda görülen model örneğinde bir öğrencinin bilgilerinin tutulduğu bir model görünmektedir. Sırasıyla açıklanmak gerekirse; <br>
**CharField** => Kısa karakterlerin girişi için oluşturulan alandır. <br>
**TextField** => Uzun açıklamalar için girişin sağlanacağı alandır. <br>
**IntegerField** => Sayısal ifadelerin barındırılğı alandır. <br>

## MODELİ VERİ TABANINA KAYIT ETMEK
**makemigrations** => Modeli veri tabanına kayıt etmeye hazır eder. <br>
**migrate** => Modeli veri tabanına kayıt eder. <br>

## MODELİ PANELİ GÖNDERMEK
Oluşturulan model doğrudan panele iletilmez bu yüzden app dosyasınızda bulunan **admin.py** dosyası içerisine modeli import ettikten sonra siteyede dahil etmeniz gerekmekte. <br> <br>
<img src="/04-MODELS/img/paneleModelDahilEtmek.PNG"> <br> <br>

Modeli incelemek için yönetim paneline **/admin** ile ulaştığınızda sizlere bir kullanıcı adı bir şifre soracaktır. Peki bu bilgileri nasıl elde edeceğiz? Hadi birlikte bir kullanıcı yaratalım! 

## CREATESUPERUSER
**createsuperuser** komutu bir user oluşturmamıza olan sağlar ve yönetim paneline rahatlıkla ulaşım sağlayabiliriz <br>

## MODEL BAŞLIKLARINI DÜZENLEMEK
Örnek modelimizde öğrencilerimiz bulunmaktaydı, ve buraya belirli başlı bilgiler girdik. <br>

<img src="/04-MODELS/img/ogrenciObjeCiktisi.PNG"> <br> <br>

Görüldüğü üzere her bir öğrenci için bir obje şekilde çıktılar elde etmiş oluyoruz. İlk bakışta bir problem yokmuş gibi dursada ilerleyen zamanlarda öğrenci sayısı arttığında bizler için sorun teşkil edecek hale gelebilir. Bu yüzden her öğrenci objelerinin başlıklarını bu model için öğrencinin adı ve soyadı şekilde değiştirmek istiyoruz. <br>

<img src="/04-MODELS/img/strSelf.PNG"> <br> <br>

Objenin Son olarak düzenlenmiş hali ise; <br> <br>
<img src="/04-MODELS/img/duzenlenmisObje.PNG"> <br> <br>

## MODELİ DOMA YAZDIRKMAK
**views.py** belgesi içerisinde modeli import etmeniz gerekmekte! <br>
Ardından **Ogrenci** classı içerisinden bütün verileri **Ogrenci.objects.all()** komutu ile çekip bir değişkene atın. Son olarak veri tabanından alınan verileri bir objede toplayın, toplanılan objeyi RETURN ettirmeyi lütfen unutmayın! <br>

<img src="/04-MODELS/img/modeliEkranaYaz.PNG"> <br> <br>