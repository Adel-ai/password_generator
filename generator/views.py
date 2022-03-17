from django.shortcuts import render
from django.http import HttpResponse
from string import ascii_lowercase, ascii_uppercase
import random

# Create your views here.


def home(request):
    # the argument above is the request passed by the user/website visitor
    return render(request, 'generator/home.html', {'password': 'fuckYouB1tch!'})


def password(request):
    myPass = ''
    length = int(request.GET.get('length', 23))
    characters = ascii_lowercase

    if request.GET.get('uppercase'):
        characters += ascii_uppercase

    if request.GET.get('numbers'):
        characters += '013456789'

    if request.GET.get('special'):
        characters += '!"§$%&/()=?+*#-.,;:_@€'

    for i in range(length):
        myPass += random.choice(characters)

    return render(request, 'generator/password.html', {'password': myPass})


def about(request):
    return render(request, 'generator/about.html')
