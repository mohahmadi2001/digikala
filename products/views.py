from django.shortcuts import render,HttpResponse
from .models import Category,Product
from django.template.loader import get_template 
# Create your views here.

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()[:10]
    category_response = ""
    for c in categories:
        category_response += f'<li><a href="/category/{c.slug}">{c.name}</a></li>'
    category_response = f"<ul>{category_response}</ul>"
    
    product_response = ""
    for p in products:
        product_response += f'<li><a href="/product/{p.id}">{p.name}</a></li>'
    product_response = f"<ul>{product_response}</ul>"
    
    return HttpResponse(f"""
                        <html>
                        <head><title>digikala</title></head>
                        <body>
                        <h1>the best site</h1>
                        {category_response}
                        {product_response}
                        </body>
                        </html>           
                        """)

def product_view(request,product_id):
    try:
        p = Product.objects.get(id = product_id)
        template = get_template('products/product.html')
        return HttpResponse(template.render(context={"product":p},request=request))
    except Product.DoesNotExist:
        return HttpResponse("404 Product not found")
    
def category_view(request,slug):
    try:
        c = Category.objects.get(slug = slug)
        return HttpResponse(f"""
                        <html>
                        <head><title>digikala</title></head>
                        <body>
                        <h1>{c.name}</h1>
                        <h5>{c.parent}</h5>
                        <p>
                        {c.description}
                        </p>
                        </body>
                        </html>           
                        """)
    except Product.DoesNotExist:
        return HttpResponse("404 Product not found")