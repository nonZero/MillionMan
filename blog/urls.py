from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import PostViewSet

app_name = "blog"

router = DefaultRouter()
router.register("post", PostViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
    path("", views.PostListView.as_view(), name="list"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),
    path("create/", views.PostCreateView.as_view(), name="create"),
]
