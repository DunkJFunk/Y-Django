from django.shortcuts import render # this is god package   ADD THIS AT THE BEGINNING
from .models import Post
from django.views.generic import ListView    # for class based views

def home(request): # ADD THIS FUNCTION AT THE BEGINNING
    context = {         # adding the 'context' or data to the site
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context) # This is soup inside the website (HTML) and the context

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) # If its short enough we can actually just pass dictionaries into the render call

# Then its here with the soup

# python manage.py createsuperuser will create a new admin user for the admin page (requires database migration)
# python manage.py makemigrations will migrate your database, or if one isnt present, will completely create a new one
# python manage.py migrate will save these changes
# an admin page comes precreated so the user will automatically fit in

# class based views are like views designed around objects, sort of like selecting a tweet and it shows you a more detailed version w comments n stuff