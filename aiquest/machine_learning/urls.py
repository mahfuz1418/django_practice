from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.machine_learning_index),
    path('ai/', views.artificial_intelegence),


]
