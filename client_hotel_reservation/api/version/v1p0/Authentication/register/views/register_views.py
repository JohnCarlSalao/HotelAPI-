from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from client_hotel_reservation.models.custom_user_model import CustomUser
from ..serializers.register_serializer import UserRegistrationSerializer
from django.contrib.auth.hashers import make_password
from client_hotel_reservation.validators.user_helper import UserHelper
######## Secret Key ############
import os
import binascii

class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        errors = UserHelper.validate_data(self,request)
        
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():

            api_secret_key = generate_api_secret_key()
            user = CustomUser.objects.create(
                username = request.data['username'],
                email = request.data['email'],
                password = make_password(request.data['password']),
                api_secret_key = api_secret_key,
            )
            return Response({'message': 'User registered successfully!', 'user_id': user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def generate_api_secret_key():
    api_secret_key_bytes = os.urandom(32)
    return binascii.hexlify(api_secret_key_bytes).decode()