from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.utils import tree

class Result(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    user_image = models.ImageField(blank=True, default='', upload_to='other/user_images/')
    place = models.CharField(max_length=300, blank=True, null=True)
    points = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, default='static/images/default.png', upload_to='other/user_images/')
    points = models.CharField(max_length=300, default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username} sin profil'