from django.db import models
from .import Booking


class Pod(models.Model):
    STATUS_CHOICE = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    AKNOWLEDGEMENT_CHOICE = (
        ('ok', 'Ok'),
        ('not ok', 'Not Ok'),
    )
    booking_no = models.ForeignKey(Booking,on_delete=models.CASCADE)
    received = models.CharField(max_length=10,choices=STATUS_CHOICE)
    received_date = models.DateField(blank=True,null=True)
    aknowledgement = models.CharField(max_length=10,choices=AKNOWLEDGEMENT_CHOICE)
    remarks = models.CharField(max_length=300, blank=True,null=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.booking_no)
