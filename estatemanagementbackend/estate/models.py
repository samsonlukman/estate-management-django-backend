from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_pics = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username}, Phone number: {self.phone_number}, Verified: {self.is_verified}, profile {self.profile_pics}"

class BuildingCategory(models.Model):
    category = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category

class BuildingCondition(models.Model):
    condition = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.condition

class FurnishingType(models.Model):
    furnishing_type = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.furnishing_type

class Building(models.Model):
    BUILDING_TYPES = [
        ('apartment', 'Apartment'),
        ('flats', 'Flats'),
        ('villa', 'Villa'),
        ('bungalow', 'Bungalow'),
        ('penthouse', 'Penthouse'),
        ('room_and_parlour', 'Room and Parlour'),
        ('duplex', 'Duplex'),
        ('townhouse_terrace', 'Townhouse/Terrace'),
        ('shared_apartments', 'Shared Apartments'),
    ]

    BUILDING_CONDITIONS = [
        ('old', 'Old'),
        ('newly_built', 'Newly Built'),
        ('renovated', 'Renovated'),
    ]

    FURNISHING_TYPES = [
        ('fully_furnished', 'Fully Furnished'),
        ('unfurnished', 'Unfurnished'),
        ('semi_furnished', 'Semi-Furnished'),
    ]
    
    name = models.CharField(max_length=255)
    property_type = models.CharField(max_length=5, choices=[('sale', 'For Sale'), ('rent', 'For Rent'), ('lease', 'For Lease')])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    property_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='property_images/')
    building_type = models.CharField(max_length=20, choices=BUILDING_TYPES, default=None)
    condition = models.CharField(max_length=20, choices=BUILDING_CONDITIONS)
    furnishing = models.CharField(max_length=20, choices=FURNISHING_TYPES)
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    toilets = models.PositiveIntegerField(default=0)
    swimming_pool = models.BooleanField(default=False)
    highspeed_internet = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    dishwasher = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    garage = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}, Owner: {self.property_owner}, Price: {self.price}, " \
               f"Building Type: {self.building_type}, " \
               f"Condition: {self.condition}, Furnishing: {self.furnishing}, " \
               f"Bedrooms: {self.bedrooms}, Bathrooms: {self.bathrooms}, " \
               f"Toilets: {self.toilets}, Swimming Pool: {self.swimming_pool}, " \
               f"Internet: {self.highspeed_internet}, Gym: {self.gym}, " \
               f"Dishwasher: {self.dishwasher}, WiFi: {self.wifi}, Garage: {self.garage}"

class Land(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_posted = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}, Owner: {self.owner}, Price: {self.price}, Posted on {self.date_posted}"
