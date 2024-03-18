from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

WORLD_COUNTRIES = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia',
    'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin',
    'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
    'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia',
    'Comoros', 'Congo', 'Costa Rica', 'Cote d\'Ivoire', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark',
    'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea',
    'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana',
    'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland',
    'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan',
    'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon',
    'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia',
    'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova',
    'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
    'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama',
    'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda',
    'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe',
    'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands',
    'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria',
    'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia',
    'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States',
    'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe',
]


    
class User(AbstractUser):
    profile_pics = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    country = CountryField(blank=True, null=True, blank_label='select country')
    is_verified = models.BooleanField(default=False)
    country = models.CharField(max_length=255, blank=True, null=True)


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

    BUILDING_CATEGORIES = [
        ('building', 'Building')
    ]
    
    category = models.CharField(max_length=20, choices=BUILDING_CATEGORIES, default='building')
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255, blank=True, null=True)
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
    description = models.TextField()
    cart = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart")

    def __str__(self):
        return f"{self.name}, Owner: {self.property_owner}, Price: {self.price}, category: {self.category} " \
               f"Building Type: {self.building_type}, " \
               f"Condition: {self.condition}, Furnishing: {self.furnishing}, " \
               f"Bedrooms: {self.bedrooms}, Bathrooms: {self.bathrooms}, " \
               f"Toilets: {self.toilets}, Swimming Pool: {self.swimming_pool}, " \
               f"Internet: {self.highspeed_internet}, Gym: {self.gym}, " \
               f"Dishwasher: {self.dishwasher}, WiFi: {self.wifi}, Garage: {self.garage}"

class Land(models.Model):
    LAND_CATEGORIES = [
        ('land', 'Land')
    ]
    category = models.CharField(max_length=20, choices=LAND_CATEGORIES, default='land')
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_posted = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    country = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name}, Owner: {self.owner.username}, Price: {self.price}, Posted on {self.date_posted}, country: {self.country}"

class LandImage(models.Model):
    land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name='land_images')
    image = models.ImageField(upload_to='property_images/', null=True, blank=True)

    def __str__(self):
        return f"Image for {self.land.name}"
    


from django.conf import settings  # For accessing User model

class SavedProperty(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return f"SavedProperty - User: {self.user.username}, Building: {self.building.price}"


