from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "calen/index.html")

def kolo(request):
    return HttpResponse("Stránka s koly!")

