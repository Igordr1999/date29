from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from main.forms import UserForm, ShopForm


def index(request):
    return HttpResponse("<h1>Hello world! it's  my first live website</h1>")


def home(request):
    return redirect(main_home)


@login_required(login_url='/main/sign-in/')
def main_home(request):
    return render(request, 'main/home.html', {})


def main_sign_up(request):
    user_form = UserForm()
    shop_form = ShopForm()
    return render(request, 'main/sign_up.html', {
        'user_form': user_form,
        'shop_form': shop_form,
    })
