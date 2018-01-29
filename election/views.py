from django.http import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from election.profile.models import UserProfile

def home(request):
       return render(request, "index.html")

def deneme(request):
    return render(request, 'deneme.html', locals())

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
        else:
            return render(request, 'login_view.html')

        return redirect('/')
    else:
        return render(request, 'login_view.html')

def signup_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        parola = request.POST['parola']
        parola1 = request.POST['parola1']
        if str(parola) == str(parola1):
            user = UserProfile.objects.filter(email="email")
            if len(user) == 0:
                user = UserProfile(name = name, email = email, is_active=True   )
                user.set_password(parola)
                user.save()
            else:
                return render(request, 'signup_view.html')

            return render(request,'login_view.html')
    else:
        return render(request, 'signup_view.html')