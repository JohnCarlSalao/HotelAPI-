from rest_framework import serializers
from client_hotel_reservation.models.rooms_model import Room

class RoomSerializer(serializers.ModelSerializer):
    room_type = serializers.CharField(source='get_room_type_display')
    
    class Meta:
        model = Room
        fields = ['uid', 'hotel', 'room_no', 'room_type', 'max_guest','description']