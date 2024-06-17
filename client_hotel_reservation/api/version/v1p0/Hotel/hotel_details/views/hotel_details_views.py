from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.hotel_details_serializer import ListHotelSerializer
from client_hotel_reservation.models.hotels_model import Hotel

class HotelDetailsAPI(APIView):
    def get(self, request, *args, **kwargs):
        ### Add Field Validator Here ####

        #################################
        
        hotel_uid = request.query_params['uid']
        try:
            hotel = Hotel.objects.get(uid=hotel_uid)
        except Hotel.DoesNotExist:
            return Response({'message': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListHotelSerializer(hotel)
        
        return Response({'message': 'Success', 'data': serializer.data}, status=status.HTTP_200_OK)