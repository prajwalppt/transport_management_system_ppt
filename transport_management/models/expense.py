from django.db import models
from .import Booking


class Expense(models.Model):

    booking_no = models.ForeignKey(Booking,on_delete=models.CASCADE)
    diesel = models.IntegerField()
    fastag = models.IntegerField()
    driver_expense = models.IntegerField()
    uncertainty = models.IntegerField()
    miscellaneous = models.IntegerField()
    expense_date = models.DateField()
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return str(self.booking_no)
