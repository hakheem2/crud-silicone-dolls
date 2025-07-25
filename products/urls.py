from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),   # e.g. /products/
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),  # e.g. /products/doll-slug/
]
