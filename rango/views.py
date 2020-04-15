from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Rango says hi there <a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("This is the about page <a href='/rango/index/'>Index</a>")