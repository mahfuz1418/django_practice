from django.urls import path
from . import views


urlpatterns = [


    path('index/', views.da_index, name='data-analysis'),


]