from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#this is the where we create function/controller in laravel
def hello(request):
    return HttpResponse("Hello, World!")