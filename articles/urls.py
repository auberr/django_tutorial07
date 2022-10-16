from django.urls import path
from articles import views

app_name = 'articles'

urlpatterns = [
    path("", views.index, name="index"),
    path("write/", views.write, name="write"),
    path("<int:article_id>/edit/", views.edit, name="edit"),
    path("<int:article_id>/article_like/", views.article_like, name="article_like"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:article_id>/comment/", views.comment, name="comment"),
    path("<int:article_id>/comment/<int:comment_id>/edit", views.comment_edit, name="comment_edit"),
    path("<int:article_id>/comment/<int:comment_id>/delete", views.comment_delete, name="comment_delete"),
    path("<int:article_id>/", views.detail, name="detail"),
]