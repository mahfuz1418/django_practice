from django.urls import path
from . import views


urlpatterns = [


    path('index/', views.about_index, name='about'),
    path('forms/', views.dynamicForm, name='forms'),


]