from django.urls import path
from . import views

urlpatterns = [
    path('api/products/', views.products, name='products'),
    path('api/products/<int:id>/', views.product_detail, name='product_detail'),
    path('api/categories/', views.categories, name='categories'),
    path('api/categories/<int:id>/', views.category_detail, name='category_detail'),
    path('api/categories/<int:id>/products/', views.category_products, name='category_products'),
]
