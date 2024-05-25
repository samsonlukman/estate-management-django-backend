from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

COUNTRY_CURRENCY_MAP = {
    'Afghanistan': 'AFN',
    'Albania': 'ALL',
    'Algeria': 'DZD',
    'Andorra': 'EUR',
    'Angola': 'AOA',
    'Antigua and Barbuda': 'XCD',
    'Argentina': 'ARS',
    'Armenia': 'AMD',
    'Australia': 'AUD',
    'Austria': 'EUR',
    'Azerbaijan': 'AZN',
    'Bahamas': 'BSD',
    'Bahrain': 'BHD',
    'Bangladesh': 'BDT',
    'Barbados': 'BBD',
    'Belarus': 'BYN',
    'Belgium': 'EUR',
    'Belize': 'BZD',
    'Benin': 'XOF',
    'Bhutan': 'BTN',
    'Bolivia': 'BOB',
    'Bosnia and Herzegovina': 'BAM',
    'Botswana': 'BWP',
    'Brazil': 'BRL',
    'Brunei': 'BND',
    'Bulgaria': 'BGN',
    'Burkina Faso': 'XOF',
    'Burundi': 'BIF',
    'Cabo Verde': 'CVE',
    'Cambodia': 'KHR',
    'Cameroon': 'XAF',
    'Canada': 'CAD',
    'Central African Republic': 'XAF',
    'Chad': 'XAF',
    'Chile': 'CLP',
    'China': 'CNY',
    'Colombia': 'COP',
    'Comoros': 'KMF',
    'Congo': 'XAF',
    'Costa Rica': 'CRC',
    'Cote d\'Ivoire': 'XOF',
    'Croatia': 'HRK',
    'Cuba': 'CUP',
    'Cyprus': 'EUR',
    'Czech Republic': 'CZK',
    'Denmark': 'DKK',
    'Djibouti': 'DJF',
    'Dominica': 'XCD',
    'Dominican Republic': 'DOP',
    'Ecuador': 'USD',
    'Egypt': 'EGP',
    'El Salvador': 'USD',
    'Equatorial Guinea': 'XAF',
    'Eritrea': 'ERN',
    'Estonia': 'EUR',
    'Eswatini': 'SZL',
    'Ethiopia': 'ETB',
    'Fiji': 'FJD',
    'Finland': 'EUR',
    'France': 'EUR',
    'Gabon': 'XAF',
    'Gambia': 'GMD',
    'Georgia': 'GEL',
    'Germany': 'EUR',
    'Ghana': 'GHS',
    'Greece': 'EUR',
    'Grenada': 'XCD',
    'Guatemala': 'GTQ',
    'Guinea': 'GNF',
    'Guinea-Bissau': 'XOF',
    'Guyana': 'GYD',
    'Haiti': 'HTG',
    'Honduras': 'HNL',
    'Hungary': 'HUF',
    'Iceland': 'ISK',
    'India': 'INR',
    'Indonesia': 'IDR',
    'Iran': 'IRR',
    'Iraq': 'IQD',
    'Ireland': 'EUR',
    'Israel': 'ILS',
    'Italy': 'EUR',
    'Jamaica': 'JMD',
    'Japan': 'JPY',
    'Jordan': 'JOD',
    'Kazakhstan': 'KZT',
    'Kenya': 'KES',
    'Kiribati': 'AUD',
    'Korea, North': 'KPW',
    'Korea, South': 'KRW',
    'Kosovo': 'EUR',
    'Kuwait': 'KWD',
    'Kyrgyzstan': 'KGS',
    'Laos': 'LAK',
    'Latvia': 'EUR',
    'Lebanon': 'LBP',
    'Lesotho': 'LSL',
    'Liberia': 'LRD',
    'Libya': 'LYD',
    'Liechtenstein': 'CHF',
    'Lithuania': 'EUR',
    'Luxembourg': 'EUR',
    'Madagascar': 'MGA',
    'Malawi': 'MWK',
    'Malaysia': 'MYR',
    'Maldives': 'MVR',
    'Mali': 'XOF',
    'Malta': 'EUR',
    'Marshall Islands': 'USD',
    'Mauritania': 'MRU',
    'Mauritius': 'MUR',
    'Mexico': 'MXN',
    'Micronesia': 'USD',
    'Moldova': 'MDL',
    'Monaco': 'EUR',
    'Mongolia': 'MNT',
    'Montenegro': 'EUR',
    'Morocco': 'MAD',
    'Mozambique': 'MZN',
    'Myanmar': 'MMK',
    'Namibia': 'NAD',
    'Nauru': 'AUD',
    'Nepal': 'NPR',
    'Netherlands': 'EUR',
    'New Zealand': 'NZD',
    'Nicaragua': 'NIO',
    'Niger': 'XOF',
    'Nigeria': 'NGN',
    'North Macedonia': 'MKD',
    'Norway': 'NOK',
    'Oman': 'OMR',
    'Pakistan': 'PKR',
    'Palau': 'USD',
    'Panama': 'PAB',
    'Papua New Guinea': 'PGK',
    'Paraguay': 'PYG',
    'Peru': 'PEN',
    'Philippines': 'PHP',
    'Poland': 'PLN',
    'Portugal': 'EUR',
    'Qatar': 'QAR',
    'Romania': 'RON',
    'Russia': 'RUB',
    'Rwanda': 'RWF',
    'Saint Kitts and Nevis': 'XCD',
    'Saint Lucia': 'XCD',
    'Saint Vincent and the Grenadines': 'XCD',
    'Samoa': 'WST',
    'San Marino': 'EUR',
    'Sao Tome and Principe': 'STN',
    'Saudi Arabia': 'SAR',
    'Senegal': 'XOF',
    'Serbia': 'RSD',
    'Seychelles': 'SCR',
    'Sierra Leone': 'SLL',
    'Singapore': 'SGD',
    'Slovakia': 'EUR',
    'Slovenia': 'EUR',
    'Solomon Islands': 'SBD',
    'Somalia': 'SOS',
    'South Africa': 'ZAR',
    'South Sudan': 'SSP',
    'Spain': 'EUR',
    'Sri Lanka': 'LKR',
    'Sudan': 'SDG',
    'Suriname': 'SRD',
    'Sweden': 'SEK',
    'Switzerland': 'CHF',
    'Syria': 'SYP',
    'Taiwan': 'TWD',
    'Tajikistan': 'TJS',
    'Tanzania': 'TZS',
    'Thailand': 'THB',
    'Timor-Leste': 'USD',
    'Togo': 'XOF',
    'Tonga': 'TOP',
    'Trinidad and Tobago': 'TTD',
    'Tunisia': 'TND',
    'Turkey': 'TRY',
    'Turkmenistan': 'TMT',
    'Tuvalu': 'AUD',
    'Uganda': 'UGX',
    'Ukraine': 'UAH',
    'United Arab Emirates': 'AED',
    'United Kingdom': 'GBP',
    'United States': 'USD',
    'Uruguay': 'UYU',
    'Uzbekistan': 'UZS',
    'Vanuatu': 'VUV',
    'Vatican City': 'EUR',
    'Venezuela': 'VES',
    'Vietnam': 'VND',
    'Yemen': 'YER',
    'Zambia': 'ZMW',
    'Zimbabwe': 'ZWL',
}


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
    
    @property
    def currency(self):
        return COUNTRY_CURRENCY_MAP.get(self.country, 'USD')

    
    def __str__(self):
        return f"{self.name}, Owner: {self.property_owner}, Price: {self.currency} {self.price}, category: {self.category} " \
               f"Building Type: {self.building_type}, " \
               f"Condition: {self.condition}, Furnishing: {self.furnishing}, " \
               f"Bedrooms: {self.bedrooms}, Bathrooms: {self.bathrooms}, " \
               f"Toilets: {self.toilets}, Swimming Pool: {self.swimming_pool}, " \
               f"Internet: {self.highspeed_internet}, Gym: {self.gym}, " \
               f"Dishwasher: {self.dishwasher}, WiFi: {self.wifi}, Garage: {self.garage}"


class BuildingImage(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/', null=True, blank=True)

    def __str__(self):
        return f"Image for {self.building.name}"

class Land(models.Model):
    LAND_CATEGORIES = [
        ('land', 'Land')
    ]
    category = models.CharField(max_length=20, choices=LAND_CATEGORIES, default='land')
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_posted = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    country = models.CharField(max_length=255, blank=True, null=True)

    @property
    def currency(self):
        return COUNTRY_CURRENCY_MAP.get(self.country, 'USD')

    

    def __str__(self):
        return f"{self.name}, Owner: {self.owner.username}, Price: {self.currency} {self.price}, Posted on {self.date_posted}"

class LandImage(models.Model):
    land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/', null=True, blank=True)

    def __str__(self):
        return f"Image for {self.land.name}"
    

    


from django.conf import settings  # For accessing User model

class SavedProperty(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    class Meta:
        # Ensure each user can save a building only once
        unique_together = ['user', 'building']

    def __str__(self):
        return f"SavedProperty - User: {self.user.username}, Building: {self.building.price}"
    

class SavedLand(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    land = models.ForeignKey(Land, on_delete=models.CASCADE)

    class Meta:
        # Ensure each user can save a building only once
        unique_together = ['user', 'land']

    def __str__(self):
        return f"SavedProperty - User: {self.user.username}, Building: {self.land.price}"



