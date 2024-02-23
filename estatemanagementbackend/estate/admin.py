from django.contrib import admin
from .models import User, Land, BuildingCondition, FurnishingType, Building




admin.site.register(User)
admin.site.register(BuildingCondition)
admin.site.register(FurnishingType)

admin.site.register(Building)
admin.site.register(Land)
