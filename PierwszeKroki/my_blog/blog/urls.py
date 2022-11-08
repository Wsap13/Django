from django.urls import path
from . import views

urlpattern = [
     path("", views.strona_startowa),
     path("posts", views.posty),
     path("posts/<slug:slug>",views.post_szegol) #/posty/moj-pierwszy-post
 ]
 