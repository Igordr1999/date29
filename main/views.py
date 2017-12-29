from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello world! it's  my first live website</h1>")


def home(request):
    return render(request, 'main/home.html', {})
