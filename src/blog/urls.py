from django.urls import path

from .views import PostCreateView

urlpatterns = [
    path("new/", PostCreateView.as_view(), name="post-create"),
]
