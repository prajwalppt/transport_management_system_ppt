from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    # weight_in_kg = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    # rate = models.PositiveIntegerField()
    value = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name