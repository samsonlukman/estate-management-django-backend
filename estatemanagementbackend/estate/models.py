from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_pics = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username}, Phone number: {self.phone_number}, Verified: {self.is_verified}"


class ResidentialSubCategory(models.Model):
    ONE_BEDROOM = 'One Bedroom'
    TWO_BEDROOM = 'Two Bedroom'
    THREE_BEDROOM = 'Three Bedroom'
    PENTHOUSE = 'Penthouse'
    DUPLEX = 'Duplex'

    SUBCATEGORY_CHOICES = [
        (ONE_BEDROOM, 'One Bedroom'),
        (TWO_BEDROOM, 'Two Bedroom'),
        (THREE_BEDROOM, 'Three Bedroom'),
        (PENTHOUSE, 'Penthouse'),
        (DUPLEX, 'Duplex'),
        # Add more choices as needed
    ]

    subcategory = models.CharField(max_length=20, choices=SUBCATEGORY_CHOICES)
    # Add any other fields specific to residential sub-categories
    def __str__(self):
        return f"{self.subcategory}"

class Property(models.Model):
    PROPERTY_TYPES = [
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
        ('lease', 'For Lease'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    property_type = models.CharField(max_length=5, choices=PROPERTY_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    property_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='property_images/')  # Specify the upload path
    subcategory = models.ForeignKey(ResidentialSubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    # Add any other fields relevant to a property

    class Meta:  # Add the Meta class to solve the related_name warning
        permissions = [
            ('can_add_property', 'Can add property'),
            ('can_edit_property', 'Can edit property'),
            ('can_delete_property', 'Can delete property'),
        ]
    
    def __str__(self):
        return f"{self.title}, Owner: {self.property_owner}, Price: {self.price}, {self.property_owner}, {self.subcategory} on {self.date_posted}"
