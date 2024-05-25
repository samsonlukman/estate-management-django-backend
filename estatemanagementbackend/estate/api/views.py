from django.db.models import Q
from estate.models import *
from .serializers import *
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.middleware.csrf import get_token
from django.http import JsonResponse
from rest_framework import filters, viewsets, status, filters, generics, permissions

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

class EditProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = EditProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
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
    queryset = Building.objects.all().order_by('-id')  # Adjust the field you want to order by
    serializer_class = BuildingSerializer

class BuildingImageListCreateView(generics.ListCreateAPIView):
    queryset = BuildingImage.objects.all()
    serializer_class = BuildingImageSerializer

class BuildingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class LandListCreateView(generics.ListCreateAPIView):
    queryset = Land.objects.all().order_by('-id')
    serializer_class = LandSerializer

class LandImageListCreateView(generics.ListCreateAPIView):
    queryset = LandImage.objects.all()
    serializer_class = LandImageSerializer

class LandRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializer

# views.py
class SavedPropertyListCreateView(generics.ListCreateAPIView):
    serializer_class = SavedPropertySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SavedProperty.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SavedPropertyDeleteView(generics.DestroyAPIView):
    serializer_class = SavedPropertySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SavedProperty.objects.filter(user=self.request.user)

class SavedPropertyViewSet(viewsets.ModelViewSet):
    queryset = SavedProperty.objects.all()
    serializer_class = SavedPropertySerializer
    permission_classes = [IsAuthenticated] 

    # Ensure saving links the property to the current user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 
    
class SavedLandListCreateView(generics.ListCreateAPIView):
    serializer_class = SavedLandSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SavedLand.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SavedLandDeleteView(generics.DestroyAPIView):
    serializer_class = SavedLandSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SavedLand.objects.filter(user=self.request.user)

class SavedLandViewSet(viewsets.ModelViewSet):
    queryset = SavedLand.objects.all()
    serializer_class = SavedLandSerializer
    permission_classes = [IsAuthenticated] 

    # Ensure saving links the property to the current user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 

@api_view(['GET'])
def property_search(request):
    query = request.GET.get('query', '')
    
    building_results = Building.objects.filter(name__icontains=query)
    land_results = Land.objects.filter(name__icontains=query)

    building_serializer = BuildingSerializer(building_results, many=True)
    land_serializer = LandSerializer(land_results, many=True)

    return Response({'building_results': building_serializer.data, 'land_results': land_serializer.data})

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'building_type', 'condition', 'furnishing', 'country']

    def get_queryset(self):
        queryset = super().get_queryset()
        min_price = self.request.GET.get('min_price', None)
        max_price = self.request.GET.get('max_price', None)
        country = self.request.GET.get('country', None)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if country:
            queryset = queryset.filter(country__icontains=country)

        return queryset

class LandViewSet(viewsets.ModelViewSet):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country']

    def get_queryset(self):
        queryset = super().get_queryset()
        min_price = self.request.GET.get('min_price', None)
        max_price = self.request.GET.get('max_price', None)
        country = self.request.GET.get('country', None)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if country:
            queryset = queryset.filter(country__icontains=country)

        return queryset