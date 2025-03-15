from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # input a html in a bit
    return HttpResponse("Hello, world. You're at the newsfeed index.")
