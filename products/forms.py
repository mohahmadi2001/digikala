from django import forms

class ProductComment(forms.Form):
    email = forms.EmailField(required=True)
    title = forms.CharField(max_length=150, required=False)
    text = forms.CharField()
    rate = forms.IntegerField(max_value=5)
    product_id = forms.IntegerField()