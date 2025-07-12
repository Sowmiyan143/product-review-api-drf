from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.models import User
from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not email or not password:
        return Response({'error': 'All fields are required'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)

    user = User.objects.create_user(username=username, email=email, password=password)
    token = Token.objects.create(user=user)
    return Response({'message': 'User registered successfully', 'token': token.key}, status=201)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def logout_user(request):
    request.user.auth_token.delete()
    return Response({'message': 'Logged out successfully'}, status=200)