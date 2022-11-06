from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

miesiace = {
    "styczeń": "Ucz się Django 45 minut dziennie.",
    "luty": "Nie spożywaj alkoholu.",
    "marzec": "Oszczędzaj 20 złotych codziennie",
    "kwieceiń": "Nie jedz słodyczy",
    "maj": "Przejedź rowerem 2000 km.",
    "czerwiec": "Spotkaj wszystkich zanjomych.",
    "lipiec": "Chodź na basen 3 razy w tygodniu.",
    "sierepień": "Naucz się stać na głowie.",
    "wrzesień": "Przebiegnij maraton.",
    "październik": "Napisz bloga.",
    "listopad": "Przeczytaj zaległe lektury.",
    "grudzień": "Pokonaj św. Mikołaja.",
}

# Create your views here.


def str_glowna(request):
    miesiac = list(miesiace.keys())
    return render(request,"wyzwania/index.html",{
        "months": miesiac
    })


def miesieczne_wyzwania_przez_liczbe(request, miesiac):
    obecny_miesiac = list(miesiace.keys())
    if miesiac > len(miesiace):
        return HttpResponseNotFound("Something goes wrong")
    poprawny_miesiac = obecny_miesiac[miesiac - 1]
    redirected_path = reverse("miesieczne_wyzwanie", args=[
                              poprawny_miesiac])  # / wyzwani/miesiac
    return HttpResponseRedirect("/wyzwania/" + poprawny_miesiac)


def miesieczne_wyzwania(request, miesiac):
    try:
        wyzwanie_text = miesiace[miesiac]
        return render(request,"wyzwania/wyzwania.html", {
            "klucz": wyzwanie_text,
            "miesiac": miesiac
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
