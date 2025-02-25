from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def da_index(requests):
    return render(requests, 'DataAnalysis/data-analysis.html');