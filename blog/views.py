from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import render
from .models import post

''''
ListView
DetailView
CreateView
UpdateView
DeleteView
'''

# Create your views here.
def home(request):
    return render(request,"blog/home.html",{
        "posts":post.objects.all(),
        "title":"Blog - Home"
    })

class PostListView(ListView):
    model = post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = post
    fields = ['title','content']


    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = post
    fields = ['title','content']


    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if post.author == self.request.user :
            return True
        else :
            return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = post
    success_url = '/blog/'
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False


def about(request):
    return render(request,"blog/about.html",{
        "title":"About"
    })

