from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        phone = request.POST.get('phone', '')
        address =request.POST.get('address', '')
        user = User.objects.create_user(username=username, password=password, phone=phone, address=address)

        return redirect('/login/')

def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            return redirect('/login/')


def home(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'home.html')
        elif request.user.is_anonymous:
            return redirect('/login/')
    
    elif request.method == 'POST':
        return HttpResponse('이 요청은 POST')
    

def profile(request, username):
    if request.method == 'GET':
        user = User.objects.get(username=username)
        if user is not None:
            context = {
                "user": user
            }
        return render(request, 'profile.html', context)

        