from django.db import models
from user.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(User, related_name='like_articles', blank=True)

    def __str__(self):
        return str(self.content)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=512)
    def __str__(self):
        return f'{self.user} {self.content}'