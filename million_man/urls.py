from django.contrib import admin
from django.urls import path, include

# URLS / URLCONF
urlpatterns = [
    path("", include("expenses.urls")),
    path("blog/", include("blog.urls")),
    path("", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
]
