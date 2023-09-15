# CREATE THIS FILE AT THE BEGINNING OF THE APPLICATION
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name='blog-home'),  
    # ^ path(following command, corresponding view(or page) from module) the homepage
    # make sure to add each of these pages/urls to the original project urls file
    path("about/", views.about,name='blog-about'),  
]

