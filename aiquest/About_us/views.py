from django.http import HttpResponse
from django.shortcuts import render
from About_us.models import Teacher
from . forms import TeachersRegistration

# Create your views here.

def about_index(request):
    teachers = Teacher.objects.all()
    return render(request, 'AboutUs/about_us.html', {'thr': teachers})
    
def dynamicForm(request):
    fm = TeachersRegistration()
    fm.order_fields(field_order=['email', 'last_name', 'first_name'])
    return render(request, 'AboutUs/forms.html', {'form': fm})
    