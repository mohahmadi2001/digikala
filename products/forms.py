from django import forms
from .models import Product
from django.core.exceptions import ValidationError

class ProductCommentForm(forms.Form):
    email = forms.EmailField(required=True,label="ایمیل")
    title = forms.CharField(max_length=150, required=False,label="عنوان")
    text = forms.CharField(widget=forms.Textarea,label="متن نظر")
    rate = forms.IntegerField(max_value=5,min_value=1,label="امتیاز")
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    
    def clean_product_id(self):
        product_id = self.cleaned_data["product_id"]
        query = Product.objects.filter(pk = product_id)
        if not query.exists():
            raise ValidationError("the product id is invalid")
        return product_id
        
        