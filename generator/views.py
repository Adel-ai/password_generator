from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # the argument above is the request passed by the user/website visitor
    return HttpResponse('hi')


def page1(request):
    return HttpResponse('<h1>Welcome to page 1 </h1>')


def page2(request):
    return HttpResponse('<h1>Welcome to page 2 </h1>')


def page3(request):
    return HttpResponse('<h1>Welcome to page 3 </h1>')


def page4(request):
    return HttpResponse('<h1>Welcome to page 4 </h1>')
