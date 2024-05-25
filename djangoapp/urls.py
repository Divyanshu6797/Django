from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('all_chai/', views.all_chai, name='all_chai'),
    
    
]
