from django.db import  models
import email
from django.core.validators import RegexValidator
class Client(models.Model):

    name = models.CharField(max_length=50, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    email = models.EmailField(max_length=50,default='abc@gmail.com')
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name
