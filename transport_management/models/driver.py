from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=50, unique=True)
    phone_number = models.IntegerField(default=+91)
    aadhar_card_no = models.IntegerField(unique=True)
    liscence_no = models.CharField(max_length=50)
    liscence_expiry_date = models.DateField()
    joining_date = models.DateField()
    remarks = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name