from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.views import PostViewSet
from expenses.views import ExpenseViewSet

router = DefaultRouter()
router.register("post", PostViewSet)
router.register("expense", ExpenseViewSet)

# URLS / URLCONF
urlpatterns = [
    path("expenses/", include("expenses.urls")),
    path("", include("blog.urls")),
    path("api/", include(router.urls)),
    path("", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
]
