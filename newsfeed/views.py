from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    # input a html in a bit
    newsfeed = render_to_string('newsfeed/newsfeed.html')
    return HttpResponse(newsfeed)

