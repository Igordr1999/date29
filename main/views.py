from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse("<h1>Hello world! it's  my first live website</h1>")


def home(request):
    return redirect(main_home)


@login_required(login_url='/main/sign-in/')
def main_home(request):
    return render(request, 'main/home.html', {})

def main_sign_up(request):
    return render(request, 'main/sign_up.html', {})