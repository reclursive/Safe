from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 path('', views.home, name='home'),
 path('about', views.about, name= 'about'),
 path('profile', views.profile, name= 'profile'),
 path('accounts/signup', views.signup, name= 'signup'),
 path('login', views.login, name= 'login'),
 path('memory_new', views.memory_new, name= 'memory_new'),
 path('wellness_center', views.wellness_center, name= 'wellness_center'),
 path('memory_delete/<int:memory_id>/', views.memory_delete, name= 'memory_delete'),
 path('memory_edit/<int:memory_id>/', views.memory_edit, name= 'memory_edit'),
 path('memory_show/<int:memory_id>/', views.memory_show, name= 'memory_show'),
 path('<int:memory_id>/question1', views.test_question1, name= 'test_question1'),
 path('<int:memory_id>/question2', views.test_question2, name= 'test_question2'),
 path('<int:memory_id>/question3', views.test_question3, name= 'test_question3'),
] 

#  path('memory_delete/<int:memory_id>/', views.memory_delete, name= 'memory_delete')
#  path('memories_new/', views.make_memory, name='memories_new'),
#  path('memories_edit/<int:memory_id>/', views.memories_post, name='memories_edit'),
#  path('memories_delete/<int:memory_id>/', views.delete_post, name= 'memories_delete')