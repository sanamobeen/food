from django.shortcuts import render
from rest_framework.views import APIView
from .utils import get_expired_fooditem
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import fooditemSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from menu.models import FoodItem


class create_food_list(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request):
        serializer = fooditemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
# Create your views here.
class get_fooditemlist(APIView):
  permission_classes = [IsAuthenticated]
  def get(self,request,food_item_id=None):
    if not food_item_id:
            return Response({"error": "Required food ID"}, status=status.HTTP_400_BAD_REQUEST)
    try:
      food_item = FoodItem.objects.get(id=food_item_id )
    except FoodItem.DoesNotExist:
      return Response({"message":"food not found"},status=status.HTTP_404_NOT_FOUND)
    if  get_expired_fooditem(food_item):
          return Response({"message": "this food item is expire"}, status=400)
        
    return Response({"message": "this food item is not expire"}, status=200)
      
