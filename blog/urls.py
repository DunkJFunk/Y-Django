# CREATE THIS FILE AT THE BEGINNING OF THE APPLICATION
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.views.generic import View

urlpatterns = [
    path("", PostListView.as_view(), name='blog-home'),  # NOTE for class based views you need to actually define it as a view
    # ^ path(following command, corresponding view(or page) from module) the homepage
    # the class based views are dependant on a template
    # make sure to add each of these pages/urls to the original project urls file
    path("about/", views.about,name='blog-about'),
    path("post/new/", PostCreateView.as_view(), name="post-create"), # with <> we directly reference variables. pk stands for primary key, how we're gonna iterate thru posts
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]

# class based views look for <app>/<model>_<viewtype>.html
# since we already have a good template we can just use that