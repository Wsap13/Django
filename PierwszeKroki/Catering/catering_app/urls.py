from django.urls import path

from . import views

urlpatterns = [
    path("", views.strona_startowa, name="strona-startowa"),
    ]