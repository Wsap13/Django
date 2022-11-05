from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

miesiace = {
    "styczeń": "Get lost!",
    "luty": "You made it is a February!",
    "marzec": "Learn more you fat idiot!",
    "kwieceiń": "Oh great in this month you have birthday",
    "maj": "Its smells like freedom",
    "czerwiec": "It's getting warm outside",
    "lipiec": "Its nice outside! Weather is hot so the girls are too.",
    "sierepień": "It's last month of holidays",
    "wrześień": "School becomes.. But not for you.",
    "październik": "Now is your time to study.",
    "listopad": "Winter, winter is coming.",
    "grudzień": "Final boss... The Saint Klose",
}

# Create your views here.

def str_glowna(request):
    list_items = ""
    miesiac = list(miesiace.keys())
    for month in miesiac:
        capitalized_month = month.capitalize()
        month_path = reverse("miesieczne_wyzwanie", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"
    
    return HttpResponse(f"<ul>{list_items}</ul>")


def miesieczne_wyzwania_przez_liczbe(request, miesiac):
    obecny_miesiac = list(miesiace.keys())
    if miesiac > len(miesiace):
        return HttpResponseNotFound("Something goes wrong")
    poprawny_miesiac = obecny_miesiac[miesiac - 1]
    redirected_path = reverse("miesieczne_wyzwanie", args=[poprawny_miesiac]) # / wyzwani/miesiac
    return HttpResponseRedirect("/wyzwania/" + poprawny_miesiac)
 

def miesieczne_wyzwania(request, miesiac):
    try:
        wyzwanie_text = miesiace[miesiac]
        response_data =f"<h1>{wyzwanie_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>You fucked up!</h1>")
