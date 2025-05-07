from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegistrationSerializer,LoginSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
class registration(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self,request):
        serializers = RegistrationSerializer(data=request.data)
        if serializers.is_valid():
            customer = serializers.save()
            refresh = RefreshToken.for_user(customer)
            return Response({
                'message': "customer registration successful",
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh)
            }, status=status.HTTP_201_CREATED)
            
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class login(APIView):
    permission_classes=[permissions.AllowAny]
    
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            
            user = authenticate(request,username=email,password=password)
            
            if user is not None:
                refresh = RefreshToken.for_user(user)
                access_token  =str(refresh.access_token) 
                return JsonResponse({
                    'msg': 'Login successful',
                    'tokens': {
                        'refresh': str(refresh),
                        'access': access_token
                    }
                }, status=status.HTTP_200_OK)
            else:
                 return Response({
                    'error': 'Invalid email or password'
                }, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    