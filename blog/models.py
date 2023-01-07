from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content
