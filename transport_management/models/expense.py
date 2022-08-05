from django.db import models
from .import Booking


class Expense(models.Model):

    booking_no = models.ForeignKey(Booking,on_delete=models.CASCADE)
    diesel = models.IntegerField(blank=True,null=True)
    fastag = models.IntegerField(blank=True,null=True)
    driver_expense = models.IntegerField(blank=True,null=True)
    uncertainty = models.IntegerField(blank=True,null=True)
    miscellaneous = models.IntegerField(blank=True,null=True)
    expense_date = models.DateField()
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return str(self.booking_no)
