from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def machine_learning_index(request):
    name = "Mahfujul Islam Ahad"
    age = 25
    address = "Mirpur, Dhaka"
    Phone = "01716965615"

    details = {'name': name, 'age': age, 'address':address, 'phone':Phone}

    return render(request, 'MachineLearning/machine_learning.html', context=details);

def artificial_intelegence(request):
    return render(request, 'MachineLearning/ai.html');