# i created this
# better than the other one

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Takes in an optional setting (default is no)

    class Meta:
        model = User
        fields = ['username','email','password1','password2'] # the fields we wanna see, password 1 and 2 for confirmation

# Added form for ability to customize profile on frontend

class UserUpdateForm(forms.ModelForm):  # forms.ModelForm is like the base structure, and u can just add fields to it
    email = forms.EmailField()
    class Meta:                         # class Meta: is giving the content to the forms
        model = User
        fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']