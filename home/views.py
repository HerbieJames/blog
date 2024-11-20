from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1 style='background-color:aqua'>home</h1>")

# Create your views here.
