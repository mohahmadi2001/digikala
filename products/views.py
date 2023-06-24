from django.shortcuts import render ,get_object_or_404
from .models import Category,Product
# Create your views here.

def product_list_view(request):
    products = Product.objects.all()[:10]
    context = {'products': products}
    return render(
        template_name='products/product-list.html',
        request=request,
        context=context,
    )
   
def product_single_view(request,product_id):

        p = get_object_or_404(Product,id=product_id)
        context = {"product":p}
        return render(
            template_name="products/product-single.html",
            request=request,
            context=context)
    
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