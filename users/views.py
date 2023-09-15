from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.
def register(request):
    if request.method == 'POST': # POST is the data from the form
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You can now log in!')
            return redirect('login')
    else:
        # a user creation form with captcha and shit already exists within DJANGO!!!
        form = UserRegisterForm()   # all it takes is making an instance of it
    return render(request, 'users/register.html', {'form':form})  # rendering the html n giving it content/context

# luckily its super ez to add instances of objects to forms 
@login_required
def profile(request):
    if request.method == 'POST':  # this basically asks the computer "are u talking to sqlite rn?" and gets run after the form is submitted

    # Added after forms/signals addon
        u_form = UserUpdateForm(request.POST, instance=request.user)    # u jus set it as a variable and it adds it to the model form
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)  # but remember the syntax is that of sqlite
        if u_form.is_valid() and p_form.is_valid():    # basically requiring both forms to be valid in order to update
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    
    else:
        u_form = UserUpdateForm(instance=request.user)    # u jus set it as a variable and it adds it to the model form
        p_form = ProfileUpdateForm(instance=request.user.profile)  # but remember the syntax is that of sqlite
    # context is like the content of the actual website, which is defined as a dictionary, like in the blog/views.py
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)