from django.urls import path
from . import views


urlpatterns = [


    path('index/', views.dl_index, name='deep-learning'),


]