from rest_framework import serializers
from .models import FoodItem
class fooditemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ['name', 'description', 'price', 'manufacturing_date', 'expiration_date', 'created_by']