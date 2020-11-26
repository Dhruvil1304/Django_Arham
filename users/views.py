from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data["username"]
            messages.success(request,f"{username} is successfully created..now you can log in ")
            return redirect('login')
        else:
            return render(request, "users/register.html", {
                "form": form
            })

    form=UserRegisterForm()
    return render(request,"users/register.html",{
        "form":form
    })

@login_required(login_url='login')
def profile(request):
    return render(request,"users/account.html")