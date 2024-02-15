# estate/admin.py

from django.contrib import admin
from .models import User, ResidentialSubCategory, Property

admin.site.register(User)
admin.site.register(ResidentialSubCategory)
admin.site.register(Property)
