from django.urls import path
from user import views

urlpatterns =[
    path('signup/', views.signup),
    path('login/', views.user_login),
    path('home/', views.home),
    path('<str:username>/profile/', views.profile),
]