from rest_framework.urls import path

from .views import CategoryListCreateView, CategoryDetailView, ProductListCreateView, ProductDetailView, InventoryListCreateView, InventoryDetailView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='categories_list_create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='categories_retrieve_update_destroy'),
    path('products/', ProductListCreateView.as_view(), name='products_list_create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products_retrieve_update_destroy'),
    path('inventory/', InventoryListCreateView.as_view(), name='inventory_list_create'),
    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name='inventory_retrieve_update_destroy'),   
]