from django.db import models
from user.models import User

# Create your models here.

class Article(models.Model):
    title = models.Charfield(max_length=255)
    content = models.Charfield(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, ondelete=models.CASCADE)

    def __str__(self):
        return str(self.content)
