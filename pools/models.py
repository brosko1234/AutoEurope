from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(max_length=600)
    email = models.EmailField(max_length=75)
    comment_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=600)
    comments = GenericRelation(Comments)


class UserV(models.Model):
    user = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    type = models.CharField(max_length=15)
