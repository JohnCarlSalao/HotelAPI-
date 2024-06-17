from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.room_details_serializer import ListRoomSerializer
from client_hotel_reservation.models.rooms_model import Room

class RoomDetailsAPI(APIView):
    def get(self, request, *args, **kwargs):
        
        room_uid = request.query_params['uid']
        try:
            room = Room.objects.get(uid=room_uid)
        except Room.DoesNotExist:
            return Response({'message': 'Room not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListRoomSerializer(room)
        
        return Response({'message': 'Success', 'data': serializer.data}, status=status.HTTP_200_OK)