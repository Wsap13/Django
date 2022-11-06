from django.urls import path
from . import views

urlpatterns = [
    path("", views.str_glowna, name="glowna"), #/wyzwania/ (taka trochę strona główna)
    path("<int:miesiac>", views.miesieczne_wyzwania_przez_liczbe),
    path("<str:miesiac>", views.miesieczne_wyzwania, name="miesieczne_wyzwanie")
    
]
 