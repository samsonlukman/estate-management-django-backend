from rest_framework import serializers
from estate.models import User, ResidentialSubCategory, Property

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'profile_pics', 'phone_number', 'about']

class ResidentialSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidentialSubCategory
        fields = ['id', 'subcategory']

class PropertySerializer(serializers.ModelSerializer):
    property_owner = UserSerializer()
    subcategory = ResidentialSubCategorySerializer()

    class Meta:
        model = Property
        fields = ['id', 'title', 'description', 'property_type', 'price', 'property_owner', 'date_posted', 'image', 'subcategory']
