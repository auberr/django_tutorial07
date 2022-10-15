from django.urls import path
from user import views

urlpatterns =[
    path('signup/', views.signup),
    path('login/', views.user_login, name="login"),
    path('<str:username>/profile/', views.profile),
]