from typing import Any, Dict
from django import forms
from django.contrib.auth import authenticate
from .models import User

class UserLogin(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserLogin, self).__init__(*args, **kwargs)
        
    email = forms.EmailField(
        widget=forms.EmailInput({"class":"form-control"}),
        required=True
        )
    password = forms.CharField(
        widget=forms.PasswordInput({"class":"form-control"}),
        required=True
        )
    
    def clean(self) -> Dict[str, Any]:
        clean_data = super().clean()
        user = authenticate(
            self.request,
            username=clean_data["email"],
            password=clean_data["password"]
            )
        if user is not None:
            clean_data["user"] = user
            return clean_data
        else:
            raise forms.ValidationError("credential is invalid")
    

class RegisterUSer(forms.Form):
    password1 = forms.CharField(
        widget=forms.PasswordInput({"class":"form-control"}),
        required=True,
        label="کلمه عبور"
        )
    password2 = forms.CharField(
        widget=forms.PasswordInput({"class":"form-control"}),
        required=True,
        label="تکرار کلمه عبور"
        )
    class Meta:
        model = User
        fields = {
            "first_name",
            "last_name",
            "email",
            "mobile",
            "password",
        }
        
    def clean(self) -> Dict[str, Any]:
        clean_data = super().clean()
        password1 = clean_data.pop("password1",None)
        password2 = clean_data.pop("password2",None)
        if password1 != password2:
            self.add_error("password2",forms.ValidationError(
                "در وارد کردن رمز عبور دقت کنید"),code="invalid"
            )
            clean_data.setdefault("password",password1)
        return clean_data
    
    def save(self,commit: bool=...) -> Any:
        user = super().save(commit)
        user.setPassword(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user