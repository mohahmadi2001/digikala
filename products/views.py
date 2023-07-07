from django.shortcuts import render ,get_object_or_404, redirect
from .models import Category,Product,Comment
from .forms import ProductCommentModelForm
# Create your views here.

def product_list_view(request):
    page = int(request.GET.get('page',1))
    query = Product.objects.all()
    q= request.GET.get('q','')
    if q:
        query = query.filter(name__contains=q)
    page_size =10
    products = query[(page-1) * page_size:page*page_size]
    context = {'products': products}
    return render(
        template_name='products/product-list.html',
        request=request,
        context=context,
    )
   
def product_detail_view(request,pk):
        p = get_object_or_404(Product,pk=pk)
        if request.method == "GET":
            form = ProductCommentModelForm(initial={"product":p})
        elif request.method == "POST":
            form = ProductCommentModelForm(request.POST)
            if form.is_valid():    
                form.save()
                return redirect("products:product-detail",pk=pk)
        context = {
            "product":p,
            "product_sellers": p.sellers_last_price,
            "comment_form":form,
            }
        return render(
            template_name="products/product-detail.html",
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