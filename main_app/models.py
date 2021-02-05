from django.db import models
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import AbstractUser, User
import django.utils.timezone

# Create your models here.
# class Memory(models.Model):
#     name = models.CharField(max_length=250, default='')
#     # image = models.URLField((""), max_length=1000, default='')
#     text = models.CharField(max_length=20000, default='')
#     def __str__(self):
#         return self.memory

# class Profile(AbstractUser):
#     name = models.ForeignKey(username, on_delete=models.CASCADE, default=1, related_name="users")
#     email = models.CharField(max_length=50)