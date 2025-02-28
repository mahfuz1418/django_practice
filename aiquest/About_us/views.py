from django.http import HttpResponse
from django.shortcuts import render
from About_us.models import Teacher

# Create your views here.

def about_index(request):
    teachers = Teacher.objects.all()
    return render(request, 'AboutUs/about_us.html', {'thr': teachers})
    