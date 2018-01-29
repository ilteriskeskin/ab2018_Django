from django.http import *
from django.shortcuts import render

def home(request):
    if request.method == 'GET':
        ad = request.GET['ad']
        email = request.GET['email']
    return render(request, 'index.html', {"name": ad, "email": email})

def deneme(request):
    return render(request, 'deneme.html', locals())