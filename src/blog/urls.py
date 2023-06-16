from django.urls import path

from .views import (
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostDetailView,
    PostLikeView,
)

urlpatterns = [
    path("new/", PostCreateView.as_view(), name="post-create"),
    path("<int:post_id>/update/", PostUpdateView.as_view(), name="post-update"),
    path(
        "<int:post_id>/delete/",
        PostDeleteView.as_view(),
        name="post-delete",
    ),
    path("<int:post_id>/", PostDetailView.as_view(), name="post-detail"),
    path("<int:post_id>/like/", PostLikeView.as_view(), name="post-like"),
]
