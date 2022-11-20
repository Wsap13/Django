from django.db import models


class pracownicy(models.Model):
    imie = models.CharField(null= False,max_length=45)
    naziwsko = models.CharField(null= False,max_length=45)
    stanowisko = models.CharField(null= False,max_length=45)
    pensja = models.DecimalField(null= False,max_digits=14, decimal_places=2)  
    pesel = models.IntegerField(default=0000000,null= False) 

class dostawca(models.Model):
    towary = models.CharField(null= False,max_length=45)
    nazwa_dostawcy = models.CharField(default='dostawca',null= False,max_length=90)
    ilosc = models.IntegerField(default='0')
    cena = models.DecimalField(null= False,max_digits=14, decimal_places=2)

class magazyn(models.Model):
    towary = models.CharField(null= False,max_length=45)
    ilosc = models.IntegerField(null= False)
    data_przydatnosci = models.DateTimeField(null= False,auto_now=False, auto_now_add=False)
    dostawca_towaru = models.ForeignKey(dostawca, on_delete=models.CASCADE)

class posilki(models.Model):
    posilek_nazwa = models.CharField(null= False,max_length=50)
    cena = models.FloatField(null= False)
    typ = models.CharField(default='normalny',null= False, max_length=50)

class klient(models.Model):
    zamowienie = models.CharField(null= False,max_length=50)
    do_zaplaty = models.DecimalField(null= False,max_digits=14, decimal_places=2)
    adres_klienta = models.CharField(null= False,max_length=50)
    posilk_klienta = models.ForeignKey(posilki, on_delete=models.CASCADE)

class faktura(models.Model):
    suma = models.DecimalField(null= False,max_digits=14, decimal_places=2)
    rozliczenia=models.DecimalField(null= False,max_digits=14, decimal_places=2)
    data = models.DateField()
    dostawca_towaru = models.ForeignKey(dostawca, on_delete=models.CASCADE)
    klient_id = models.ForeignKey(klient, on_delete=models.CASCADE)
# Create your models here.
