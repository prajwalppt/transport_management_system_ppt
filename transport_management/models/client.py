from django.db import  models

class Client(models.Model):

    name = models.CharField(max_length=50, unique=True)
    phone_number = models.IntegerField(default=+91)
    email = models.EmailField(max_length=50,default='abc@gmail.com')
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name
