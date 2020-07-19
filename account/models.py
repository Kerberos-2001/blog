from django.db import models
from django import forms
from django.contrib.auth import get_user_model
# Create your models here.

AUTHER = get_user_model()

class Auther(models.Model):
    number = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=150)
    conform_password = models.CharField(max_length=150)
    profilepic = models.ImageField(upload_to='profile', blank=True, null=True)
    user = models.OneToOneField(AUTHER, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


