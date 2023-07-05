from .views import product_list_view , product_detail_view ,create_comment ,category_view
from django.urls import path
app_name = "products"
urlpatterns = [
    path('',product_list_view,name="product-list"),
    path('<int:product_id>',product_detail_view,name="product-detail"),
    path('comments/<int:product_id>',create_comment,name="create_comment"),
    path('category/<slug:slug>',category_view)
]
