from django.urls import path
from . import views


urlpatterns = [


    path('index/', views.bloogs_index, name='bloogs'),


]