from django.db import models
from . import Client, Vehicle, Product, Driver

class Booking(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('deliverd', 'Delivered'),
        ('approved', 'Approved'),
        ('complete', 'Complete'),
        ('decline', 'Decline'),   
        
    )
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    no_of_product = models.IntegerField()
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE)
    weight_in_tons =  models.IntegerField()
    location_from = models.CharField(max_length=70)
    location_to= models.CharField(max_length=70)
    loading_date = models.DateField()
    freight_amount = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICE,default='pending')
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)