from django.shortcuts import render

# Create your views here.

def strona_startowa(request):
  return render(request, "blog/index.html")

def posty(request):
   return render(request, "blog/all-posts.html")

def posty_szczegol(request):
  pass