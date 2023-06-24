from .views import product_list_view , product_single_view , category_view
from django.urls import path

urlpatterns = [
    path('',product_list_view),
    path('<int:product_id>',product_single_view),
    path('category/<slug:slug>',category_view)
]
