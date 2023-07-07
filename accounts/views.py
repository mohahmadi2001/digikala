from django.shortcuts import render,redirect
from accounts.forms import UserLogin,UserRegisterFrom
from django.contrib.auth import login,logout
# Create your views here.

def login_view(request):
    if request.method == "GET":
        form = UserLogin()
    else:
        form = UserLogin(request.POST, request=request)
        if form.is_valid():
            user = form.cleaned_data["user"]
            login(request=request,user=user)
            return redirect("accounts:user_info_view")
    context={
        "form":form
    }
    return render(
        request,
        "accounts/login-view.html",
        context
    )

def user_register_view(request):
    status = 200
    if request.method == "GET":
        form = UserRegisterFrom()
    else:
        form = UserRegisterFrom(request.POST, request=request)
        if form.is_valid():
            user = form.cleaned_data["user"]
            user = form.save(commit=True)
            login(request=request,user=user)
            return redirect("accounts:user_info_view")
        else:
            status = 400
    context={
        "form":form
    }
    return render(
        request,
        "accounts/register-view.html",
        context,
        status=status
    )
    
def user_info_view(request):
    return render(request,"accounts/user-info.html",{})

def logout_user(request):
    logout(request)
    return redirect("accounts:user_info_view")