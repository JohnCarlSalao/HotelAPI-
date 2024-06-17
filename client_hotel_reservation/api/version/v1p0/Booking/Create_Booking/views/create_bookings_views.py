from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.create_bookings_serializers import CreateBookingSerializer
from client_hotel_reservation.models.bookings_model import Booking
from client_hotel_reservation.models.availability_model import Availability
from client_hotel_reservation.models.rooms_model import Room
from rest_framework_simplejwt.authentication import JWTAuthentication
from client_hotel_reservation.validators.user_helper import UserHelper
from client_hotel_reservation.validators.booking_checker import BookingChecker

class CreateBookingAPI(APIView):
    authentication_classes = [JWTAuthentication]
    def post(self,request, *args, **kwargs):
        ### Add Field Validator Here ####
        errors = UserHelper.validate_user(self,request)

        errors = BookingChecker.validate_room_uid(self,request)

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        #################################
        serializer = CreateBookingSerializer(data=request.data)
        
        if serializer.is_valid():
            room_id = request.query_params['rooms']
            room = Room.objects.get(uid=room_id)

            check_in = serializer.data['check_in']
            check_out = serializer.data['check_out']
            
            booking = Booking.objects.create(
                user = request.user,
                rooms = room,
                booking_name = request.data['booking_name'],
                phone_num = request.data['phone_num'],
                no_of_guest = request.data['no_of_guest'],
                description = request.data['description'],
            )

            errors = BookingChecker.validate_existing_booking_date(self,room,check_in,check_out)

            if errors:
                booking.delete()
                return Response({'message': 'Room is not available for the specified period.'}, status=status.HTTP_400_BAD_REQUEST)
           
            Availability.objects.create(booking=booking, check_in=check_in, check_out=check_out)
            serialized_booking = serializer.data
            serialized_booking['user'] = request.user.email
            serialized_booking['rooms'] = {
                'uid': room.uid,
                'room_number': room.room_no,
                'room_type': room.room_type,
            }
            return Response({'message': 'Booking Successfuly Created', 'data' : serialized_booking}, status=status.HTTP_201_CREATED)
        
        return Response({'message': 'error', 'error' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)