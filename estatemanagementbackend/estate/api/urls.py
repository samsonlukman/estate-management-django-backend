# urls.py
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('get-csrf-token/', views.get_csrf_token, name="get-csrf-token"),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('upload/building/', BuildingUploadListCreateView.as_view(), name='upload-building'),
    path('upload/land/', LandUploadListCreateView.as_view(), name='upload-land'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('user/', get_user_details, name='get_user_details'),
    path('building-conditions/', BuildingConditionListCreateView.as_view(), name='building-condition-list-create'),
    path('furnishing-types/', FurnishingTypeListCreateView.as_view(), name='furnishing-type-list-create'),
    path('user/login/', views.user_login, name='user_login'),
    path('user/logout/', views.user_logout, name='user_logout'),
    path('buildings/', BuildingListCreateView.as_view(), name='building-list-create'),
    path('buildings/<int:pk>/', BuildingRetrieveUpdateDestroyView.as_view(), name='building-retrieve-update-destroy'),
    path('land/', LandListCreateView.as_view(), name='land-list-create'),
    path('land/<int:pk>/', LandRetrieveUpdateDestroyView.as_view(), name='land-retrieve-update-destroy'),
]
