from rest_framework import generics
from estate.models import *
from .serializers import *
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.middleware.csrf import get_token
from django.http import JsonResponse

User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    logout(request)
    return Response({'message': 'User logged out successfully'}, status=status.HTTP_200_OK)

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(user)
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

    
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_details(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class BuildingConditionListCreateView(generics.ListCreateAPIView):
    queryset = BuildingCondition.objects.all()
    serializer_class = BuildingConditionSerializer

class FurnishingTypeListCreateView(generics.ListCreateAPIView):
    queryset = FurnishingType.objects.all()
    serializer_class = FurnishingTypeSerializer


class BuildingUploadListCreateView(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingUploadSerializer

class LandUploadListCreateView(generics.ListCreateAPIView):
    queryset = Land.objects.all()
    serializer_class = LandUploadSerializer


class BuildingListCreateView(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class BuildingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class LandListCreateView(generics.ListCreateAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializer

class LandRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
