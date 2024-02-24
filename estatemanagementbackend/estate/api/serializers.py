# serializers.py
from rest_framework import serializers
from estate.models import User, Land, BuildingCondition, FurnishingType, Building
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    profile_pics = serializers.ImageField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'about', 'password', 'profile_pics']
        

    def validate(self, data):
        password = data.get('password')
        try:
            # Use Django's password validation to ensure a strong password
            validate_password(password=password)
        except ValidationError as e:
            # Print the validation error details
            print(f"Validation error: {e.messages}")
            raise serializers.ValidationError(e.messages)

        return data

    def to_representation(self, instance):
        return {
            'status': 'error',
            'message': 'Validation error',
            'errors': self.errors,
        }

    def create(self, validated_data):
        try:
            # Try to create the user
            user = User.objects.create_user(**validated_data)
            return user
        except ValidationError as ve:
            # Handle validation error and include it in the response
            self.errors = ve.messages
            return None
        except Exception as e:
            # Print the error and raise the exception again
            print(f"Error creating user: {e}")
            raise e


class BuildingUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = [
            'name', 'building_type', 'price',
            'bedrooms', 'bathrooms', 'toilets', 'property_owner', 'swimming_pool',
            'highspeed_internet', 'gym', 'dishwasher', 'wifi', 'garage',
            'property_type', 'building_type', 'condition', 'furnishing', 'image'
        ]

class LandUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = ['name', 'owner', 'price', 'description', ]

    def to_internal_value(self, data):
        try:
            return super().to_internal_value(data)
        except serializers.ValidationError as e:
            raise serializers.ValidationError({
                'error': 'Invalid input',
                'details': e.detail
            })

class BuildingConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingCondition
        fields = '__all__'

class FurnishingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FurnishingType
        fields = '__all__'



class BuildingSerializer(serializers.ModelSerializer):
    property_owner = UserSerializer()

    class Meta:
        model = Building
        fields = '__all__'

class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = '__all_'
