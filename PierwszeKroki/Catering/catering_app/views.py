from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import pracownicy,magazyn,posilki,klient,faktura
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework import permissions
from django.contrib.auth.models import User


class PracownicyLista(generics.ListCreateAPIView):
    queryset = pracownicy.objects.all()
    


# Create your views here.
