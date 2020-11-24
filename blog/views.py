from django.shortcuts import render
from .models import post


# Create your views here.
def home(request):
    return render(request,"blog/home.html",{
        "posts":post.objects.all(),
        "title":"Blog - Home"
    })

def about(request):
    return render(request,"blog/about.html",{
        "title":"About"
    })

