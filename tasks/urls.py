from django.urls import path
from . import views

app_name= "tasks"

urlpatterns =[
    path('', views.index, name="index"),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('login/', views.logout_user, name='logout'),
    path('tasks/', views.task_list, name='tasks'),
    path('tasks/new/', views.create_task, name='create_task'),
    path('tasks/<int:pk>/edit/', views.update_task, name='edit_task'),
    path('tasks/<int:pk>/delete/', views.delete_task, name='delete_task'),
]