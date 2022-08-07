from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Footfall analysis on the hotspots of the campus")

def home(request):
    return render(request,"main.html")

    