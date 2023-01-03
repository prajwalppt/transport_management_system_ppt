from django.db import models
from django.core.validators import RegexValidator

class Driver(models.Model):
    name = models.CharField(max_length=50, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    aadhar_card_no = models.IntegerField(unique=True)
    liscence_no = models.CharField(max_length=50)
    liscence_expiry_date = models.DateField()
    joining_date = models.DateField()
    remarks = models.CharField(max_length=220, blank=True,null=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name