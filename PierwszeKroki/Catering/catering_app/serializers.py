from rest_framework import serializers
from .models import pracownicy, magazyn, posilki, klient
import string
import datetime


class pracownicySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pracownicy
        fields = ['imie', 'nazwisko', 'stanowisko', 'stanowisko', 'pensja', 'pesel']

    def validate_imie(self, value):
        if value[0] in string.ascii_lowercase:
            raise serializers.ValidationError(
                "Imiona zaczynają się z dużej litery"
            )
        else:
            return value

    def validate_nazwisko(self, value):
        if value[0] in string.ascii_lowercase:
            raise serializers.ValidationError(
                "Nazwiska zaczynają się z dużej litery"
            )
        else:
            return value

    def validate_pensja(self, value):
        if value.any() <= 0:
            raise serializers.ValidationError(
                "Pensja nie może być mniejsza równa zero"
            )
        else:
            return value

class magazynSerializer(serializers.HyperlinkedModelSerializer):
    dostawca_towaru = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='') #zrobic widok i uzupelnic
        
    class Meta:
            model = magazyn
            fields = ['towary', 'ilosc','data_przydatnosci', 'dostawca_towaru']
    
    def validate_ilosc(self, value):
        if value.any() < 0:
            raise serializers.ValidationError(
                "Ilosc towaru nie może być mniejsza niż zero"
            )
        else:
            return value

    def validate_dataPrzydatnosci(self, value):
        if value.any() < datetime.datetime.now:
            raise serializers.ValidationError(
                "Nie można przechowywać żywności po terminie."
            )
        else:
            return value

class posilkiSerializer(serializers.HyperlinkedModelSerializer):
        
    class Meta:
            model = posilki
            fields = ['posilek_nazwa', 'cena','typ']

    def validate_cena(self, value):
        if value.any() <= 0:
            raise serializers.ValidationError(
                "Cena nie może być mniejsza równa zero"
            )
        else:
            return value

class klientSerializer(serializers.HyperlinkedModelSerializer):
        
    class Meta:
            model = klient
            fields = ['zamowienie', 'do-zaplaty','adres_klienta']

    def validate_cena(self, value):
        if value.any() <= 0:
            raise serializers.ValidationError(
                "Cena nie może być mniejsza równa zero"
            )
        else:
            return value            