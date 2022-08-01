from django.db import models

from . import Vehicle

class VehicleMaintanance(models.Model):
    STATUS_CHOICE = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    vehicle_no = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    under_maintanance = models.CharField(max_length=10,choices=STATUS_CHOICE, default='')
    date_of_initialization = models.DateField()
    odometer_reading = models.IntegerField()
    oil_changed = models.CharField(max_length=10,choices=STATUS_CHOICE)
    spare_parts_replaced = models.CharField(max_length=300)
    total_cost_of_maintenance = models.IntegerField()

    def __str__(self):
        return str(self.vehicle_no)