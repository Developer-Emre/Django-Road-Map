## İLK PROJE
İlk proje adımlamalara göre ilerlendiğinde oluşturulur.

## FARKLI SAYFALAR NASIL OLUŞTURULUR ? 
İşin temelinde index.html nasıl oluşturulup tanımlanıyor ise farklı sayflarda aynı mantıkla oluşturulup yönlendirilir.

Örnek vermek gerkirse;
About sayfası için **views.py** içerisinde yeni bir fonksiyon oluşturulur. <br> <br>
<img src="img/views.PNG"> <br>

Oluşturulan about sayfası **urls.py** içerisinde yeni bir path olarak tanımlanır <br> <br>
<img src="img/urls.PNG"> <br>

Artık url alanına /hakkimizda yazarak sayfaya ulaşabilirsin.<br> <br>
<img src="img/web.PNG">

## SAYFALAR ARASI GEÇİŞ NASIL SAĞLANIR ?
Sayfalar arası geçişte mantık çok basittir. 2 Farklı yol izlenilebilir; <br>
**1.Yol**
Doğrudan oluşturulan sayfalara href yoluyla dizine ulaşmak.<br> <br>
<img src="img/dizin.PNG">

**2.yol**
urls.py dosyasında name ile yolların isimleri tanımlanır.<br>
<img src="img/urls-name.PNG"> <br> <br>

İstenilen sayfalar içerisinde ise yönlendirmeler ekte görüldüğü gibi yönlendirilir <br>
<img src="img/indexUrl.PNG">

## STYLE & JAVASCRİPT DOSYALARI NASIL TANIMLANIR
**static** adında bir klasör açılır <br>

Bu klasör içerisine istenilen css,js yada img dosyaları yerleştirilebilir. <br>
<img src="img/staticStyleJsImg.PNG"> <br> <br>

İkinci bir yol olarak da **{% load static %}** kullanılabilir.<br>
HTML girişinde **{% load static %}** yüklenilir ve head içersinde linkleme yöntemiyle css çekilir <br>

<img src="img/loadStaticStyle.PNG"> <br> <br>
**Bu yapılan işlemler aynı mantıkla js dosyasıları içinde geçerlidir.**