from rest_framework.urls import path

from .views import ReviewListCreateView, ReviewDetailView


urlpatterns = [
    path('reviews/', ReviewListCreateView.as_view(), name='reviews_list_create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='reviews_retrieve_update_destroy'),
]