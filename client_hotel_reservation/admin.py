from django.contrib import admin
from client_hotel_reservation.models.bookings_model import Booking
from client_hotel_reservation.models.hotels_model import Hotel
from client_hotel_reservation.models.rooms_model import Room
from client_hotel_reservation.models.availability_model import Availability
from client_hotel_reservation.models.custom_user_model import CustomUser
from django.contrib.auth.admin import UserAdmin

class HotelAdmin(admin.ModelAdmin):
    readonly_fields = ('uid',)

class RoomAdmin(admin.ModelAdmin):
    readonly_fields = ('uid',)

class BookingAdmin(admin.ModelAdmin):
    readonly_fields = ('uid',)

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password','api_secret_key')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('api_secret_key',)
    

admin.site.register(Hotel,HotelAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Booking,BookingAdmin)
admin.site.register(Availability)
admin.site.register(CustomUser,CustomUserAdmin)
