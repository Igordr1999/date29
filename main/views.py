from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from main.forms import UserForm, ShopForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate
from django.contrib.auth import login


def index(request):
    return HttpResponse("<h1>Hello world! it's  my first live website</h1>")


def home(request):
    return redirect(main_home)


@login_required(login_url='/main/sign-in/')
def main_home(request):
    return render(request, 'main/home.html', {})


@login_required(login_url='/main/sign-in/')
def main_account(request):
    return render(request, 'main/account.html', {})


@login_required(login_url='/main/sign-in/')
def main_orders(request):
    return render(request, 'main/orders.html', {})


def main_sign_up(request):
    user_form = UserForm()
    shop_form = ShopForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        shop_form = ShopForm(request.POST, request.FILES)

        if user_form.is_valid() and shop_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_shop = shop_form.save(commit=False)
            new_shop.owner = new_user
            new_shop.save()

            login(request, authenticate(
                username = user_form.cleaned_data["username"],
                password=user_form.cleaned_data["password"]
            ))

            return redirect(main_home)
    return render(request, 'main/sign_up.html', {
        'user_form': user_form,
        'shop_form': shop_form,
    })
