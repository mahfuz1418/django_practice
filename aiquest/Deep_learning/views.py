from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Create your views here.
def dl_index(request):
    return render(request, 'DeepLearning/deep_learning.html');