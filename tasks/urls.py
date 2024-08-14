from django.urls import path
from . import views

app_name= "tasks"

urlpatterns =[
    path('', views.index, name="index"),
    path('register/', views.register_user, name='register'),
]