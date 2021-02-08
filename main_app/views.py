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
  memories = Memory.objects.filter(user_id=request.user.id)
  context = {'memories': memories}
  return render(request, 'User/profile.html', context)

def signup(request):
  error_message=''
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request)
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
  form = MemoryForm(request.POST)
  if request.method == "POST":
    # prefill = {'user': request.user}
    current_user = request.user
    form = MemoryForm(request.POST, {'user': current_user})
    if form.is_valid():
      memory = form.save(commit=False)
      memory.user = request.user
      memory.save()
      return redirect('profile')
    else:
      print(form.errors)
      error_message = 'Invalid post input'
  current_user = request.user
  form = MemoryForm()
  context= {'form' : form, 'error_message': error_message, 'user': current_user}
  return render(request, 'User/memory_new.html', context)

def memory_delete(request, memory_id):
  Memory.objects.get(id = memory_id).delete()
  return redirect('profile')

# def edit_memory(request, memory_id):
#   current_memory = Memory.objects.get(id=memory_id)
#   if request.method == 'POST':
#     form = MemoryForm(request.POST, instance=current_memory)
#     if form.is_valid():
#       memory = Memory.objects.get(id=memory_id)
#       if request.POST['name']:
#         memory.name = request.POST['name']
#         user_id = request.POST['user']
#         user = Memory.objects.get(id=user_id)
#         memory.user = user
#       memory.save()
#       return redirect('profile')
#     else:
#       print(form.errors)
#       error_message = 'Invalid input'
#   form = Edit_Post_Form(initial={'title' : current_post.title, 'body' : current_post.body})
#   context = {'form' : form, 'post' : current_post}
#   return render(request, 'User/memory_edit.html', context)