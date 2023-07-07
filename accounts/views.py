from django.shortcuts import render,redirect
from accounts.forms import UserLogin,RegisterUSer
from django.contrib.auth import login
# Create your views here.

def login_view(request):
    if request.method == "GET":
        form = UserLogin()
    else:
        form = UserLogin(request.POST, request=request)
        if form.is_valid():
            user = form.cleaned_data["user"]
            login(request=request,user=user)
            return redirect("")
    context={
        "form":form
    }
    return render(
        request,
        "accounts/login-view.html",
        context
    )

def user_register_view(request):
    if request.method == "GET":
        form = UserLogin()
    else:
        form = UserLogin(request.POST, request=request)
        if form.is_valid():
            user = form.cleaned_data["user"]
            user = form.save(commit=True)
            login(request=request,user=user)
            return redirect("")
    context={
        "form":form
    }
    return render(
        request,
        "accounts/login-view.html",
        context
    )
    
