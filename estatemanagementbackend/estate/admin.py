from django.contrib import admin
from .models import User,SavedLand, BuildingImage, Land, SavedProperty, BuildingCondition, FurnishingType, Building, LandImage


admin.site.register(BuildingImage)
admin.site.register(User)
admin.site.register(BuildingCondition)
admin.site.register(FurnishingType)
admin.site.register(LandImage)
admin.site.register(Building)
admin.site.register(Land)
admin.site.register(SavedProperty)
admin.site.register(SavedLand)
