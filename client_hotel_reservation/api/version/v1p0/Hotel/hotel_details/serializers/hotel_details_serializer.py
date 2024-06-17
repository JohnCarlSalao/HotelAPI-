from rest_framework import serializers
from client_hotel_reservation.models.hotels_model import Hotel

class ListHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['uid', 'hotel_name', 'location', 'hotel_image','description']