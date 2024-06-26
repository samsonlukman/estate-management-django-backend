# serializers.py
from rest_framework import serializers
from estate.models import *
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
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'about', 'password', 'profile_pics', 'country']
        

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

class EditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'about', 'country']

        username = serializers.CharField(required=False)
        first_name = serializers.CharField(required=False)
        last_name = serializers.CharField(required=False)
        email = serializers.EmailField(required=False)
        phone_number = serializers.CharField(required=False)
        about = serializers.CharField(required=False)
        profile_pics = serializers.ImageField(required=False)  
        country = serializers.CharField(required=False)
        about = serializers.CharField(required=False)
        
        
class BuildingSerializer(serializers.ModelSerializer):
    property_owner = UserSerializer()
    currency = serializers.ReadOnlyField()

    class Meta:
        model = Building
        fields = '__all__'

    


class SavedPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedProperty
        fields = '__all__' 
    
        
class SavedLandSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedLand
        fields = '__all__' 

class BuildingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingImage
        fields = '__all__'
        
class BuildingUploadSerializer(serializers.ModelSerializer):
    images = BuildingImageSerializer(many=True, read_only=True)

    class Meta:
        model = Building
        fields = [
            'name', 'building_type', 'price',
            'bedrooms', 'bathrooms', 'toilets', 'property_owner', 'swimming_pool',
            'highspeed_internet', 'gym', 'dishwasher', 'wifi', 'garage',
            'property_type', 'building_type', 'condition', 'furnishing', 'country', 'images'
        ]

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        building = Building.objects.create(**validated_data)

        for image_data in images_data.values():
            BuildingImage.objects.create(building=building, image=image_data)

        return building

class LandImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandImage
        fields = '__all__'

class LandUploadSerializer(serializers.ModelSerializer):

    images = LandImageSerializer(many=True, read_only=True)

    class Meta:
        model = Land
        fields = ['name', 'owner', 'price', 'description', 'country', 'images']

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        land = Land.objects.create(**validated_data)

        for image_data in images_data.values():
            LandImage.objects.create(land=land, image=image_data)

        return land
    
class BuildingConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingCondition
        fields = '__all__'

class FurnishingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FurnishingType
        fields = '__all__'




class LandSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    currency = serializers.ReadOnlyField()

    class Meta:
        model = Land
        fields = '__all__'

    
