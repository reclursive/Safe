from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'),
 path('about', views.about, name= 'about'),
 path('profile', views.profile, name= 'profile'),
 path('accounts/signup', views.signup, name= 'signup'),
 path('login', views.login, name= 'login'),
#  path('memories_new/', views.make_memory, name='memories_new'),
#  path('memories_edit/<int:memory_id>/', views.memories_post, name='memories_edit'),
#  path('memories_delete/<int:memory_id>/', views.delete_post, name= 'memories_delete')
]