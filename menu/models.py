from django.db import models
from customer.models import Customer
from django.conf import settings
class FoodItem(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    manufacturing_date = models.DateField()
    expiration_date = models.DateField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
