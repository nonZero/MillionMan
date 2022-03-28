"""million_man URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path


# VIEW FUNCTIONS
def home(request):
    return HttpResponse("Hello world!!!")


def mazal_tov(request, person_name: str):
    return HttpResponse(f"Mazal Tov {person_name}!!! ")


def squared(request, n: int):
    return HttpResponse(f"{n}^2 = {n ** 2}")

def add(request, a: int, b: int):
    return HttpResponse(f"{a} + {b} = {a+b}")

def price(request, name: str, price: int):
    return HttpResponse(f"The price of {name} is {price:.2f} NIS.")


# URLS / URLCONF
urlpatterns = [
    path('', home),
    path('mazal-tov/<person_name>/', mazal_tov),
    path('sqr/<int:n>/', squared),
    path('add/<int:a>/<int:b>/', add),
    path('price/<name>/<int:price>/', price),
    path('price/<int:price>/<name>/', price),
    path('sale/<name>/', price, {
        "price": 3,
    }),
    path('drink/<int:price>/', price, {
        "name": 'coffee',
    }),
    path('admin/', admin.site.urls),
]
