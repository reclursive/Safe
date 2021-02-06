from django.contrib import admin

# Register your models here.
from .models import Memory, Question
from django.contrib.auth.admin import UserAdmin

UserAdmin.list_display = ('username', 'email', 'is_active', 'date_joined', 'is_staff')

admin.site.register(Memory)
admin.site.register(Question)