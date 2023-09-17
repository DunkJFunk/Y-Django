from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# a model is like a pattern for the database
class Post(models.Model):  # basically inheriting from models
    title = models.CharField(max_length=100) # "Character Field". also u can add a bunch of arguments
    content = models.TextField() # A text field is unrestricted text instead of characters
    date_posted = models.DateTimeField(default=timezone.now)  # Selecting the current time
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # If the user gets deleted, delete the post\

    def __str__(self):
        return self.title # makes it easier to read in the sql

# Inside the command line,
# python manage.py shell
# from blog.models import Post
# from django.contrib.auth.models import User
# User.objects.all()
# User.objects.first()
# User.objects.filter(username='PorthosKG')
# user = User.objects.filter(username='PorthosKG').first()     # grabs this
# user.id
# user.pk           ^ these 2 do the same thing
# user = User.objects.get(id=1)      once retrieving the id number you can just reference it from there
# post_1 = Post(title='Blog 1', content='First Post Content!', author=user)
# post_1.save()              actually saves it to the database
# post_2 = Post(title='Blog 2', content='Second Post Content!', author=user)
# post_2.save()
# post = Post.objects.first()          selecting the current post for detailing
# post.content
# post.date_posted                      you can call modules or attributes off it
# post.author.email                     u can just keep stacking em on
# user.post_set                         the syntax is modelname_set for ALL of the users posts
# user.post_set.all()                   executing them
# user.post_set.create(title='Blog 3', content='Third Post Content!')           creating a new post THROUGH the user
# Post.objects.all()                        print all posts