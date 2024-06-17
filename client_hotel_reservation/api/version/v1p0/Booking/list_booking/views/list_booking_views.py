from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.list_booking_serializer import ListBookingSerializer
from client_hotel_reservation.models.bookings_model import Booking
from rest_framework_simplejwt.authentication import JWTAuthentication
from client_hotel_reservation.validators.user_helper import UserHelper

class ListBookingAPI(APIView):
    authentication_classes = [JWTAuthentication]
    def get(self,request):
        
        errors = UserHelper.validate_user(self,request)
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        
        bookings = Booking.objects.filter(user = request.user,is_archive = False)
        serializer = ListBookingSerializer(bookings,many=True)
        
        return Response({'message': 'Success', 'data': serializer.data}, status=status.HTTP_200_OK)