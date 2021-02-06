from django.db import models
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
import django.utils.timezone

# Create your models here.


class Memory(models.Model):
    name = models.CharField(max_length=250, default='')
    img = models.ImageField(upload_to = "images/", blank=True)
    text = models.CharField(max_length=20000, default='', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    


class Question(models.Model):
    text = models.CharField(max_length=20000, default='What year is it?')
    answer = models.CharField(max_length=20000, default='2021')
    