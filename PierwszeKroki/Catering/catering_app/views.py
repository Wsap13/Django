from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet


class PracownicyFilter(FilterSet):
    min_pensja = NumberFilter(field_name='pensja', lookup_expr='gte')
    max_pensja = NumberFilter(field_name='pensja', lookup_expr='lte')
    pracownik_name = AllValuesFilter(field_name='name')

    class Meta:
        model = Pracownicy
        fields = ['min_pensja', 'max_pensja', 'pracownik_name']

class PracownicyList(generics.ListCreateAPIView):
    queryset = Pracownicy.objects.all()
    serializer_class = PracownicySerializer
    name = 'pracownicy-list'
    search_fields = ['imie', 'nazwisko']
    filter_class = PracownicyFilter
    permission_classes = [IsAuthenticated]

class PracownicyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pracownicy.objects.all()
    serializer_class = PracownicySerializer
    name = 'pracownicy-detail'
    permission_classes = [IsAuthenticated]

class MagazynList(generics.ListCreateAPIView):
    queryset = Magazyn.objects.all()
    serializer_class = MagazynSerializer
    name = 'magazyn-list'
    permission_classes = [IsAuthenticated]

class MagazynDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Magazyn.objects.all()
    serializer_class = MagazynSerializer
    name = 'magazyn-detail'
    permission_classes = [IsAuthenticated]    

class PosilkiList(generics.ListCreateAPIView):
    queryset = Posilki.objects.all()
    serializer_class = PosilkiSerializer
    name = 'posilki-list'
    permission_classes = [IsAuthenticated]

class PosilkiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posilki.objects.all()
    serializer_class = PosilkiSerializer
    name = 'posilki-detail'
    permission_classes = [IsAuthenticated]

class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'Klient-list'
    permission_classes = [IsAuthenticated]

class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'Klient-detail'
    permission_classes = [IsAuthenticated]

class ZamowieniaList(generics.ListCreateAPIView):
    queryset = Zamowienia.objects.all()
    serializer_class = ZamowieniaSerializer
    name = 'Zamowienia-list'
    permission_classes = [IsAuthenticated]

class ZamowieniaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zamowienia.objects.all()
    serializer_class = ZamowieniaSerializer
    name = 'Zamowienia-detail'
    permission_classes = [IsAuthenticated]


# class PracownicyApiView(APIView):
#     def get(self,request):
#         allPracownicy=Pracownicy.objects.all().values()
#         return Response({"Message":"Lista pracowników","Pracownicy lsita":allPracownicy})
    
#     def post(self,request):
#         Pracownicy.objects.create(imie=request.data["imie"],
#                                 nazwisko=request.data["nazwisko"],
#                                 stanowisko=request.data["stanowisko"],
#                                 pensja=request.data["pensja"],
#                                 pesel=request.data["pesel"]
#                                 )
#         pracownik=Pracownicy.objects.all().filter(id=request.data["imie"]).values()
#         return Response({"Message":"Pracownik dodany","Pracownik":pracownik})

# class PracownicyList(generics.ListCreateAPIView):
#     queryset = pracownicy.objects.all()
#     serializer_class = pracownicySerializer
#     name = 'pracownicy-list'



# Create your views here.
