from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.list_hotel_serializers import ListHotelSerializer
from client_hotel_reservation.models.hotels_model import Hotel

class ListHotelAPI(APIView):
    def get(self,request):
        hotels = Hotel.objects.all()
        serializer = ListHotelSerializer(hotels,many=True)
        
        return Response({'message': 'Success', 'data': serializer.data}, status=status.HTTP_200_OK)