from django.urls import path

from . import views

urlpatterns = [
    path("", views.strona_startowa, name="strona-startowa"),
    path("posty", views.posty, name="posty"),
    path("posts/<slug:slug>", views.posty_szczegol,
         name="posty-szczegol")  # /posts/my-first-post
]