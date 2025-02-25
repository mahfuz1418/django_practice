from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def about_index(request):
    return render(request, 'AboutUs/about_us.html')
    