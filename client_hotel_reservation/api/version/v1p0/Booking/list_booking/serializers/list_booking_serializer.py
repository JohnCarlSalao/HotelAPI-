from rest_framework import serializers
from client_hotel_reservation.models.bookings_model import Booking
from client_hotel_reservation.models.availability_model import Availability

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ['booking', 'check_in', 'check_out']

class ListBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['uid','rooms', 'booking_name', 'phone_num','no_of_guest','description']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['schedule'] = AvailabilitySerializer(instance.availability_set.all(),many=True).data
        return rep