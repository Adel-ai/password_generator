from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # the argument above is the request passed by the user/website visitor
    return render(request, 'generator/home.html', {'password': 'fuckYouB1tch!'})


def password(request):
    return render(request, 'generator/password.html')
