from django.db import  models

class Vehicle(models.Model):
    registration_no = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=50)
    manufacture_company = models.CharField(max_length=50)
    insurance_valid_till = models.DateField()
    permit_tax_valid_till = models.DateField()
    fitness_valid_till = models.DateField()

    def __str__(self):
        return self.registration_no