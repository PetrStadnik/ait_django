from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    a = 5
    b = a**2
    c = 4
    p = [13, "Liška", 999.99]
    return render(request, "calen/index.html", {"a": a, "mocnina": b, "kriterium": c, "pole":p})

def kolo(request):
    return HttpResponse("Stránka s koly!")


def udalosti(request):
    ud = Udalost.objects.filter(jmeno="Narozeniny")
    return render(request, "calen/udalosti.html", {"udalosti": ud})

