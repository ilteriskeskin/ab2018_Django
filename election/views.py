from django.http import *
from django.shortcuts import render

def home(request):
    return render(request, 'index.html', locals())

def deneme(request):
    return render(request, 'deneme.html', locals())