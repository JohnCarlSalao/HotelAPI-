from rest_framework import serializers
from client_hotel_reservation.models.custom_user_model import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2']