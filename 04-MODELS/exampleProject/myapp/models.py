from django.db import models

# Create your models here.
class Ogrenci(models.Model):
    isim = models.CharField(("Adınız"), max_length=50)
    soyisim = models.CharField(("Soyadınız"), max_length=50)
    no = models.IntegerField(("Numaranız"))
    aciklama = models.TextField(("Açıklama"), max_length=500)
    
    def __str__(self) -> str:
        return self.isim