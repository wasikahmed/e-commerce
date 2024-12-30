from django.urls import path

from .views import CustomerListCreateView, CustomerDetailView
from .models import Customer

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customers_list_create'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customers_retrieve_update_destroy'),
]
