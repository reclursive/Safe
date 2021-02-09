from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from PIL import Image
# from SAFE.settings import MEDIA_ROOT


from .models import Memory 
from .forms import MemoryForm


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
    form = MemoryForm(request.POST, request.FILES, {'user': current_user})
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



def memory_show(request, memory_id):
  current_user = request.user
  memory = Memory.objects.get(id=memory_id)
  if request.user.is_authenticated:
    context = {
      'user': current_user,
      'memory': memory,
      'img': memory.img
      }
    return render(request, 'Memory/totalview.html', context)
  else:
    return redirect('acounts/signup')




def memory_edit(request, memory_id):
  memory = Memory.objects.get(id=memory_id)
  if request.method == 'POST':
    if request.POST['name'] != '':
      memory.name = request.POST['name']
      memory.save()
      return redirect('profile')
    else:
      print(form.errors)
      error_message = 'Invalid input'
      return redirect('profile')
  context= {'memory': memory}
  return render(request, 'User/memory_edit.html', context)


@login_required
def test_question1(request, memory_id):
    # question = Question.objects.get(id=memory_id)
    # context= {'memory': memory}
    return render(request, 'Test/question1.html')

@login_required
def test_question2(request, memory_id):
  # memory = Memory.objects.get(id=memory_id)
    # question = Question.objects.get(id=memory_id)
  return render(request, 'Test/question2.html')

@login_required
def test_question3(request, memory_id):
    # question = Question.objects.get(id=memory_id)
    return render(request, 'Test/question3.html')





















# def memory_edit(request, memory_id):
#   current_memory = Memory.objects.get(id=memory_id)
#   form = UpdateMemoryName(request.POST)
#   if request.method == 'POST':
#     # current_user = request.user
#     # form = UpdateMemoryName(request.POST)
#     if form.is_valid():
#       memory = Memory.objects.get(id=memory_id)
#       if request.POST['name']:
#         memory.name = request.POST['name']
#         user = Memory.objects.get(id=user_id)
#         memory.user = user
#       memory.save()
#       return redirect('profile')
#     else:
#       print(form.errors)
#       error_message = 'Invalid input'
#   context= {'form' : form, 'error_message': error_message, 'user': current_user}
#   return render(request, 'User/memory_edit.html')

# def edit_memory(request, memory_id):
  # current_memory = Memory.objects.get(id=memory_id)
  # if request.method == 'POST':
  #   current_user = request.user

  #   form = MemoryForm(request.POST, {'user': current_user})
  #   if form.is_valid():
  #     memory = Memory.objects.get(id=memory_id)
  #     if request.POST['name']:
  #       memory.name = request.POST['name']
  #       user_id = request.POST['user']
  #       user = Memory.objects.get(id=user_id)
  #       memory.user = user
  #     memory.save()
  #     return redirect('profile')
  #   else:
  #     print(form.errors)
  #     error_message = 'Invalid input'
  # form = Edit_Post_Form(initial={'title' : current_post.title, 'body' : current_post.body})
  # context = {'form' : form, 'post' : current_post}
  # return render(request, 'User/memory_edit.html', context)