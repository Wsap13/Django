from django.db import models


class pracownicy(models.Model):
    imie = models.CharField(max_length=45)
    naziwsko = models.CharField(max_length=45)
    stanowisko = models.CharField(max_length=45)
    pensja = models.IntegerField()
    pensja = models.IntegerField()   

class dostawca(models.Model):
    towary = models.CharField(max_length=45)
    ilosd = models.IntegerField()
    cena = models.FloatField()

class magazyn(models.Model):
    towary = models.CharField(max_length=45)
    ilosc = models.IntegerField()
    data_przydatnosci = models.DateTimeField(auto_now=False, auto_now_add=False)
    dostawca_towaru = models.ForeignKey(dostawca, on_delete=models.CASCADE)

class posilki(models.Model):
    posilek_nazwa = models.CharField(max_length=50)
    cena = models.FloatField()

class klient(models.Model):
    zamowienie = models.CharField(max_length=50)
    do_zaplaty = models.FloatField()
    adres_klienta = models.CharField(max_length=50)
    posilk_klienta = models.ForeignKey(posilki, on_delete=models.CASCADE)

class faktura(models.Model):
    suma = models.FloatField()
    rozliczenia=models.FloatField()
    data = models.DateField()
    dostawca_towaru = models.ForeignKey(dostawca, on_delete=models.CASCADE)
    klient_id = models.ForeignKey(klient, on_delete=models.CASCADE)
# Create your models here.
