from django.http import *
from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        ad = request.GET['ad']
        email = request.GET['email']
        data = "%s, %s" % (ad, email)
        return render(request, 'index.html', {"data": data})

    else:
        return render(request, "index.html")

def deneme(request):
    return render(request, 'deneme.html', locals())