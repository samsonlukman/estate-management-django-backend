# estate/views.py

from rest_framework import generics
from estate.models import User, ResidentialSubCategory, Property
from .serializers import UserSerializer, ResidentialSubCategorySerializer, PropertySerializer

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ResidentialSubCategoryListView(generics.ListCreateAPIView):
    queryset = ResidentialSubCategory.objects.all()
    serializer_class = ResidentialSubCategorySerializer

class ResidentialSubCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ResidentialSubCategory.objects.all()
    serializer_class = ResidentialSubCategorySerializer

class PropertyListView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
