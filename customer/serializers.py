from rest_framework import serializers
from .models import Customer
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username','email','password']
        extra_kwargs = {
            'password' : {'write_only':True}
        }

    def create(self,validated_data):
        return Customer.objects.create_user(**validated_data)
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

       