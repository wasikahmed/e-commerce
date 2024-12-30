from rest_framework.urls import path

from .views import CartListCreateView, CartDetailView

urlpatterns = [
    path('carts/', CartListCreateView.as_view(), name='carts_list_create'),
    path('carts/<int:pk>/', CartDetailView.as_view(), name='carts_retrieve_update_destroy'),
]