from django.urls import path

from .views import CustomerListCreateView, CustomerDetailView, StaffListCreateView, StaffDetailView
from .models import Customer, Staff

urlpatterns = [
    path('staff/', StaffListCreateView.as_view(), name='staff_list_create'),
    path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff_retrieve_update_destroy'),
    path('customers/', CustomerListCreateView.as_view(), name='customers_list_create'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customers_retrieve_update_destroy'),
]
