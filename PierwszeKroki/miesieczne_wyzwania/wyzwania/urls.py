from django.urls import path
from . import views

urlpatterns = [
    path("<int:miesiac>", views.miesieczne_wyzwania_przez_liczbe),
    path("<str:miesiac>", views.miesieczne_wyzwania)
    
]
