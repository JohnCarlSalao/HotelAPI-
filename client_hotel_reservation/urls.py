from django.urls import path
from .api.version.v1p0.Hotel.list_hotel.views.list_hotel_views import ListHotelAPI
from .api.version.v1p0.Hotel.hotel_details.views.hotel_details_views import HotelDetailsAPI
from .api.version.v1p0.Booking.Create_Booking.views.create_bookings_views import CreateBookingAPI
from .api.version.v1p0.Booking.list_booking.views.list_booking_views import ListBookingAPI
from .api.version.v1p0.Booking.Cancel_Booking.views.cancel_booking_views import UpdateBookingAPI
from .api.version.v1p0.Rooms.list_rooms.views.list_rooms_views import ListRoomsAPI
from .api.version.v1p0.Rooms.room_details.views.room_details_views import RoomDetailsAPI
from .api.version.v1p0.Authentication.login.views.login_views import UserLoginView
from .api.version.v1p0.Authentication.register.views.register_views import UserRegistrationAPIView
from .api.version.v1p0.Search.views.search_view import SearchAPIView


urlpatterns = [
    ############ Authenticate ################
    path('login/', UserLoginView.as_view(), name = 'client_login'),
    path('register/', UserRegistrationAPIView.as_view(), name = 'client_register'),

    ############ Hotels #############

    path('hotels/list/', ListHotelAPI.as_view(), name = 'client_list_hotel'),
    path('hotels/details/', HotelDetailsAPI.as_view(), name = 'client_details_hotel'),

    ############ bookings #############

    path('booking/add/', CreateBookingAPI.as_view(), name = 'client_add_booking'),
    path('booking/list/', ListBookingAPI.as_view(), name = 'client_list_booking'),
    path('booking/cancel/', UpdateBookingAPI.as_view(), name = 'client_cancel_booking'),

    ############ Rooms ###############

    path('rooms/list/', ListRoomsAPI.as_view(), name = 'client_list_rooms'),
    path('rooms/details/', RoomDetailsAPI.as_view(), name = 'client_details_rooms'),


    ############ Search ###############
    path('search/', SearchAPIView.as_view(), name = 'client_search'),
]