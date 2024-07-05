from django.db import models
from sellers.models import Seller

class Sale(models.Model):
    order_number = models.CharField(max_length=100, primary_key=True)
    date = models.DateField()
    country = models.CharField(max_length=100)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=100)
    sellers = models.ManyToManyField(Seller)

    class Meta:
        indexes = [
            models.Index(fields=['order_number'], name='order_number_idx'),
        ]
    
    def __str__(self):
        return self.order_number
