import uuid
from .hotels_model import Hotel
from .availability_model import Availability
from django.db import models

class Room(models.Model):
    
    uid = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    hotel = models.ForeignKey(Hotel , on_delete= models.CASCADE, null=True)
    room_no = models.IntegerField(null=True)
    ROOM_TYPE = (
        ('S', 'Suite'),
        ('SA', 'Studio Apartment'),
        ('PS', 'Presidential Suite'),
        ('ES', 'Executive Suite'),
        ('DHR', 'Deluxe_Hotel Rooms'),
        ('SHR', 'Studio_Hotel Rooms'),
        ('ROHR', 'Room_Only Hotel_Rooms'),
        ('SSR', 'Standard_Suite Rooms'),
        ('PSHR', 'Presidential Suite Hotel Rooms'),
        ('ASHB', 'Apartment Style Hotel Bedroom'),
    )
    room_type = models.CharField(max_length=4, null= True, choices=ROOM_TYPE)
    room_image = models.ImageField(null=True)
    is_available = models.BooleanField(default=True)
    max_guest = models.IntegerField(null=True)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = 'Rooms'
        
    def __str__(self):
        return str(self.room_no)