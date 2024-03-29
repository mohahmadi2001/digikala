from .views import product_list_view , product_detail_view  ,category_view
from django.urls import path
app_name = "products"
urlpatterns = [
    path('',product_list_view,name="product-list"),
    path('<int:pk>',product_detail_view,name="product-detail"),
    path('category/<slug:slug>',category_view),
]
