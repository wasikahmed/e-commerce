from rest_framework.urls import path

from .views import OrderListCreateView, OrderDetailView

urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='orders_list_create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='orders_retrieve_update_destroy'),
]