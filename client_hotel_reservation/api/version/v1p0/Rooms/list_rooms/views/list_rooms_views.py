from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.rooms_serializer import ListRoomSerializer
from client_hotel_reservation.models.rooms_model import Room
from client_hotel_reservation.models.hotels_model import Hotel


class ListRoomsAPI(APIView):
    def get(self, request, *args, **kwargs):
        
        hotel_uid = request.query_params['uid']

        try:
            hotel = Hotel.objects.get(uid=hotel_uid)
        except Hotel.DoesNotExist:
            return Response({'message': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)
        
        rooms = Room.objects.filter(hotel=hotel_uid,is_available=True)
        serializer = ListRoomSerializer(rooms, many=True)
        
        return Response({'message': 'Success', 'data': serializer.data}, status=status.HTTP_200_OK)
