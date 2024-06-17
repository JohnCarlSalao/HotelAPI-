from rest_framework import serializers
from client_hotel_reservation.models.bookings_model import Booking
from datetime import datetime

def convert_date_format(date_str):
    try:
        # Convert the date string to a date object in 'yyyy/mm/dd' format
        date_obj = datetime.strptime(date_str, '%Y/%m/%d').date()
        # Format the date object as a string in 'yyyy-mm-dd' format
        formatted_date = date_obj.strftime('%Y-%m-%d')
        return formatted_date
    except ValueError:
        raise serializers.ValidationError("Invalid date format. Date must be in 'yyyy/mm/dd' format.")

class CustomDateField(serializers.DateField):
    def to_internal_value(self, value):
        return convert_date_format(value)

class CreateBookingSerializer(serializers.ModelSerializer):
    check_in = CustomDateField(required=True)
    check_out = CustomDateField(required=True)

    class Meta:
        model = Booking
        fields = ['user', 'rooms', 'booking_name', 'phone_num', 'no_of_guest', 'check_in', 'check_out', 'description']
        extra_kwargs = {
            'booking_name': {'required': True},
            'phone_num': {'required': True},
            'no_of_guest': {'required': True},
        }

    # def validate_rooms(self, value):
        
    #     if not value.is_available(self.initial_data['check_in'], self.initial_data['check_out']):
    #         raise serializers.ValidationError("Room is not available for the specified period.")
    #     return value