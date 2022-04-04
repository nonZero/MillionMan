from django.contrib import admin
from django.urls import path, include

# URLS / URLCONF
urlpatterns = [
    path("", include("expenses.urls")),
    path("admin/", admin.site.urls),
]
