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
import random

from django.contrib import admin
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import path, include


def my_view(request: HttpRequest):
    if "my_random_number" not in request.session:
        request.session["my_random_number"] = random.randint(1, 10)

    resp = render(
        request,
        "cookie_demo.html",
        {
            # "d": request.session,
            "d": request.COOKIES,
            "secret": request.session["my_random_number"],
        },
    )
    return resp


# URLS / URLCONF
urlpatterns = [
    path("", my_view),
    path("my-expenses/", include("expenses.urls")),
    path("admin/", admin.site.urls),
]
