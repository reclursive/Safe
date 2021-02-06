from django.forms import ModelForm, ModelChoiceField
from django import forms
from .models import Memory
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from datetime import datetime





class MemoryForm(ModelForm):
    name = forms.CharField(max_length=250)
    text = forms.CharField(max_length=20000)
    class Meta:
        user = User
        model = Memory
        fields = ['name', 'img', 'text', 'user']


# class Memory_Form(ModelForm):
#     user = MemoryModelChoiceField(queryset=Memory.objects.all())
#     name = models.CharField(max_length=250, default='')
#     img = models.ImageField(upload_to = "images/", blank=True)
#     text = models.CharField(max_length=20000, default='', blank=True)
#     class Meta:
#         model = Memory
#         fields = ['name', 'img', 'text']

# class RegisterForm(UserCreationForm):
#     class Meta:
#         fields = ("name", "email", "password")
#         help_texts= ""

# class EditUserForm(UserChangeForm):
#     username = forms.CharField(max_length=254, required=False)
#     password=None
#     class Meta:
#         model = Profile
#         exclude = ("password1", "password2")
#         fields = ("username")
#         help_texts= ""

# class Memory_Form(ModelForm):
#     class Meta:
#         model = Memory
#         fields = ['name', 'text', 'image' ]

