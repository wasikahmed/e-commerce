from django.urls import path
from .views import SellerListCreateView, SellerDetailView

urlpatterns = [
    path('sellers/', SellerListCreateView.as_view(), name='sellers_list_create'),
    path('sellers/<int:pk>/', SellerDetailView.as_view(), name='sellers_retrieve_update_destroy'),
]
