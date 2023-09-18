from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 # this is god package   ADD THIS AT THE BEGINNING
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView   # for class based views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

def home(request): # ADD THIS FUNCTION AT THE BEGINNING
    context = {         # adding the 'context' or data to the site
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context) # This is soup inside the website (HTML) and the context

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) # If its short enough we can actually just pass dictionaries into the render call

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'  # we say posts because thats what it is in the home template
    ordering = ['-date_posted']  # organizes from latest first instead of oldest first
    paginate_by = 10

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'  # we say posts because thats what it is in the home template
    ordering = ['-date_posted']  # organizes from latest first instead of oldest first
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username')) # settings the user object as the selected user of the url
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

# Since we cant add decorators to classes we use mixins to add functionality
class PostCreateView(LoginRequiredMixin, CreateView): # By adding the login mixin we require you to be logged in
    success_url = "/"
    model = Post
    fields = ['title','content'] # what specifications we want for each new post
    def form_valid(self, form):
        form.instance.author = self.request.user # basically setting the author id to the current logged in user
        return super().form_valid(form) # whole line just reruns the validity check since it technically gets overwritten AFTER the first check

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # whenever we add the test mixin you have to write the test function it runs
    success_url = "/"
    model = Post
    fields = ['title','content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
# python manage.py createsuperuser will create a new admin user for the admin page (requires database migration)
# python manage.py makemigrations will migrate your database, or if one isnt present, will completely create a new one
# python manage.py migrate will save these changes
# an admin page comes precreated so the user will automatically fit in

# class based views are like views designed around objects, sort of like selecting a tweet and it shows you a more detailed version w comments n stuff

# the shell code for Pagination examples/notes \/

# In [2]: posts = ['1','2','3','4','5']
# In [3]: p = Paginator(posts, 2)
# In [4]: p.num_pages
# Out[4]: 3
# In [5]: for page in p.page_range:
#             print(page)
# 1
# 2
# 3
# In [6]: p1 = p.page(1)
# In [7]: p1
# Out[7]: <Page 1 of 3>
# In [8]: p1.number
# Out[8]: 1
# In [9]: p1.object_list
# Out[9]: ['1', '2']
# In [10]: p1.has_previous()
# Out[10]: False
# In [11]: p1.has_next()
# Out[11]: True
# In [12]: p1.next_page_number()
# Out[12]: 2