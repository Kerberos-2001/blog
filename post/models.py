from django.contrib.auth.models import AbstractUser
from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from account.models import Auther



class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    createdAt = models.DateField(auto_now=True)
    updatedAt = models.DateField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)
    count = models.IntegerField()
    image = models.ImageField(upload_to='blog')
    auther = models.ForeignKey(Auther, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

def slugfield(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slugfield, sender=Blog)