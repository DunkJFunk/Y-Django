from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
# Models is like the website version of classes and OOP

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)                   # One to one relationship with the user model (Cascase means to also delete profile with user, but not vice versa)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')     # Adding a default image and a directory for new images (profile pics)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):            # overrides the save model
        super().save(*args, **kwargs)           # saving the current image
        x = Image.open(self.image.path)         # opens the instance as a variable
        if x.height > 300 or x.width > 300:     # checking if its in the size range
            output_size = (300,300)             # the new size we want
            x.thumbnail(output_size)            # sizing it down
            x.save(self.image.path)             # saving it