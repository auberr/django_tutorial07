from django.urls import path
from user import views

app_name = 'user'

urlpatterns =[
    path('signup/', views.signup),
    path('login/', views.user_login, name="login"),
    path('<str:username>/profile/', views.profile, name="profile"),
    path('<str:username>/profile/follow/', views.follow, name="follow"),
]