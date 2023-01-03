from django.db import models
from .import Booking


class Payment(models.Model):
    MODE_CHOICE = (
        ('cash', 'Cash'),
        ('online', 'Online'),
    )

    booking_no = models.ForeignKey(Booking,on_delete=models.CASCADE)
    amount = models.IntegerField()
    mode = models.CharField(max_length=10,choices=MODE_CHOICE)
    transaction_no = models.CharField(max_length=220, blank=True,null=True)
    payment_date = models.DateField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.booking_no)
