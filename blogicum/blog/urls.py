from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/<int:id>/", views.post_id, name="post_id"),
    path("category/<slug:category_slug>/",
         views.category_posts, name="category_posts"),
]
