from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# from .forms import RegisterForm

from .models import Memory 
from .forms import MemoryForm
# from .forms import RegisterForm, EditUserForm

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def profile(request):
  memories = Memory.objects.all()
  context = {'memories': memories}
  return render(request, 'User/profile.html', context)

def signup(request):
  error_message=''
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('profile')
    else:
      error_message = 'Invalid sign up'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def login(request):
  return render(request, 'Registration/login.html')


# def memory_new(request, user_id):
#   current_user = User.objects.get(id=user_id)
#   MemoryForm = MemoryForm()
#   return render(request, 'profile', {
#     'user': user, 'memory_form': memory_form
#   })
@login_required
def memory_new(request):
  error_message=''
  if request.method == "POST":
    form = MemoryForm(request.POST)
    if form.is_valid():
      user = request.user
      memory = form.save(commit=False)
      user.username = user
      memory.save()
      return redirect('profile')
    else:
      print(form.errors)
      error_message = 'Invalid post input'
  current_user = request.user
  form = MemoryForm()
  context= {'form' : form, 'error_message': error_message, 'user': current_user}
  return render(request, 'User/memory_new.html', context)

# def memory_delete(request, memory_id):
#   Memory.objects.get(id = memory_id).delete()
#   return redirect('profile')

