# estate/urls.py

from django.urls import path
from .views import UserListView, UserDetailView, ResidentialSubCategoryListView, ResidentialSubCategoryDetailView, PropertyListView, PropertyDetailView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('subcategories/', ResidentialSubCategoryListView.as_view(), name='subcategory-list'),
    path('subcategories/<int:pk>/', ResidentialSubCategoryDetailView.as_view(), name='subcategory-detail'),
    path('properties/', PropertyListView.as_view(), name='property-list'),
    path('properties/<int:pk>/', PropertyDetailView.as_view(), name='property-detail'),
]
