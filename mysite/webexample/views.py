from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h1 style="text-align:center">FUSK ALL!!!</h1>')