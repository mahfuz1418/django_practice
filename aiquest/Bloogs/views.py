from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Create your views here.
def bloogs_index(request):
    return render(request, 'Bloogs/bloogs.html')