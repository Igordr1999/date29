"""date29 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from main.views import index
from main import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^main/sign-in/$', auth_views.login, {'template_name': 'main/sign_in.html'}, name="main-sign-in"),
    url(r'^main/sign-out/$', auth_views.logout, {'next_page': '/'}, name="main-sign-out"),
    url(r'^main/$', views.main_home, name='main_home'),
    url(r'^main/sign-up/$', views.main_sign_up, name='main_sign_up'),
    url(r'^main/account/$', views.main_account, name='main_account'),
    url(r'^main/orders/$', views.main_orders, name='main_orders'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
