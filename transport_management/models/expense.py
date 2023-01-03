from django.db import models
from .import Booking


class Expense(models.Model):

    booking_no = models.ForeignKey(Booking,on_delete=models.CASCADE)
    # diesel = models.IntegerField(blank=True,null=True, default=0)
    # fastag = models.IntegerField(blank=True,null=True, default=0)
    # driver_expense = models.IntegerField(blank=True,null=True, default=0)
    # uncertainty = models.IntegerField(blank=True,null=True, default=0)
    # miscellaneous = models.IntegerField(blank=True,null=True, default=0)
    diesel = models.IntegerField(default=0)
    fastag = models.IntegerField(default=0)
    driver_expense = models.IntegerField(default=0)
    uncertainty = models.IntegerField(default=0)
    miscellaneous = models.IntegerField(default=0)
    expense_date = models.DateField()
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return str(self.booking_no)
