from typing import Any
from django import forms
from .models import Product,Comment
from django.core.exceptions import ValidationError

# class ProductCommentForm(forms.Form):
#     email = forms.EmailField(required=True,label="ایمیل",widget=forms.TextInput(attrs={"class":"form-control"}))
#     title = forms.CharField(max_length=150, required=False,label="عنوان",widget=forms.TextInput(attrs={"class":"form-control"}))
#     text = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}),label="متن نظر")
#     rate = forms.IntegerField(max_value=5,min_value=1,label="امتیاز",widget=forms.TextInput(attrs={"class":"form-control"}))
#     product_id = forms.IntegerField(widget=forms.HiddenInput())
    
#     def clean_product_id(self):
#         product_id = self.cleaned_data["product_id"]
#         query = Product.objects.filter(pk = product_id)
#         if not query.exists():
#             raise ValidationError("the product id is invalid")
#         return product_id
        
class ProductCommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        widgets = {
            "email": forms.EmailInput(attrs={"class":"form-control"}),
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "text": forms.Textarea(attrs={"class":"form-control"}),
            "rate": forms.NumberInput(attrs={"class":"form-control"}),
            "product": forms.HiddenInput()
        }   
    def save(self, commit: bool = ...) -> Any:
        return super().save(commit)