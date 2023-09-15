# MAN MADE

# This file allows us to 'signal' functions, we'll be using it to automatically create an account for each user

from django.db.models.signals import post_save  # We gon need this
from django.contrib.auth.models import User     # This is the sender
from django.dispatch import receiver            # This is the reciever
from .models import Profile

@receiver(post_save, sender=User)                      # The decorator ties it all together
def create_profile(sender,instance,created,**kwargs):  # It takes in 4 arguments, as listed
    if created:
        Profile.objects.create(User=instance)          # same syntax as the sql in the shell

@receiver(post_save, sender=User)
def save_profile(sender,instance,created,**kwargs):
    instance.profile.save()

# Dont forget to add these to the users/apps.py file once u create them!