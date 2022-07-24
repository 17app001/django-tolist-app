from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('todo/<int:id>', views.view, name='view'),
    path('create/', views.create, name='create'),

]
