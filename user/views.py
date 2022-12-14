from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import User
from articles.models import Article
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

        return redirect('/user/login/')

def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('articles:index')
        else:
            return redirect('/user/login/')

def profile(request, username):
    if request.method == 'GET':
        user = User.objects.get(username=username)
        articles = Article.objects.all()
        if user is not None:
            context = {
                "user": user,
                "articles": articles
            }
        return render(request, 'profile.html', context)

def follow(request, username):
    if request.method == 'GET':
        user = request.user
        following = list(user.follow.all().values('username'))
        context = {
            'following': following
        }
        return render(request, 'profile.html', context)

    if request.method == 'POST':
        target_user = User.objects.get(username=username)
        user = request.user
        user.follow.add(target_user)
        user.save()
        return redirect('user:profile', username)