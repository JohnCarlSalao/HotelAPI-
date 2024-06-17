import uuid
from django.db import models

class Availability(models.Model):
    uid = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    booking = models.ForeignKey('client_hotel_reservation.Booking' , on_delete= models.CASCADE, null=True)
    check_in = models.DateField(null=True)
    check_out = models.DateField(null=True)
    is_archive = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Availability'
        
    def __str__(self):
        return str(self.uid)