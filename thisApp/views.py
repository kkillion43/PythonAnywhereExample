from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    myDict = {'temp1' : 'Hello I am from views.py'}

    return render(request, 'index.html', context=myDict)
