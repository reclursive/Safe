from django.forms import ModelForm, ModelChoiceField
from django import forms
from .models import Memory
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from datetime import datetime


# class RegisterForm(UserCreationForm):
#     city = CityModelChoiceField(queryset=City.objects.all())
#     class Meta:
#         model = Profile
#         fields = ("username", "city", "email",)
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

