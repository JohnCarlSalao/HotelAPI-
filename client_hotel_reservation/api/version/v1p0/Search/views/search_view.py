import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from client_hotel_reservation.models.rooms_model import Room
from ..serializers.search_serializer import RoomSerializer
from django.db.models import Q

class SearchAPIView(APIView):
    
    def post(self, request, *args, **kwargs):

        if 'location' in request.data and request.data['location'] != '':
            if 'check_in' in request.data and request.data['check_in'] != '':
                if 'check_out' in request.data and request.data['check_out'] != '':
                    if 'total_guest' in request.data and request.data['total_guest'] != '':
                        
                        location = request.data['location']
                        check_in, check_out = self.separate_dates(request)

                        total_guest = int(request.data['total_guest'])

                        available_rooms = Room.objects.filter(
                            hotel__location=location,
                            is_available=True,
                            max_guest__gte=total_guest,   
                        ).exclude(
                             Q(booking__availability__check_in__lte=check_out) & Q(booking__availability__check_out__gte=check_in) & Q(booking__availability__is_archive=False)
                        ).distinct()


                        serializer = RoomSerializer(available_rooms, many=True)

                        return Response({'message': 'Successfully retrieved available rooms.', 'data': serializer.data}, status=status.HTTP_200_OK)
    
        return Response({'error': 'Invalid search.'}, status=status.HTTP_400_BAD_REQUEST)

    def separate_dates(self, request):
        from_date_str = request.data.get('check_in', '')
        to_date_str = request.data.get('check_out', '')

        from_date = datetime.datetime.strptime(from_date_str, '%Y/%m/%d').date() if from_date_str else None
        to_date = datetime.datetime.strptime(to_date_str, '%Y/%m/%d').date() if to_date_str else None

        return from_date, to_date
