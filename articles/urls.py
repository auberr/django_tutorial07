from django.urls import path
from articles import views

app_name = 'articles'

urlpatterns = [
    path("", views.index, name="index"),
    path("write/", views.write, name="write"),
    path("<int:article_id>/edit/", views.edit, name="edit"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:article_id>/comment/", views.comment, name="comment"),
    path("<int:article_id>/", views.detail, name="detail"),
]