from django.db import models

class Seller(models.Model):
    seller_id = models.CharField(max_length=100, primary_key=True)
    language = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
  
    class Meta:
        indexes = [
            models.Index(fields=['seller_id'], name='seller_id_idx'),
        ]
    
    def __str__(self):
        return self.seller_id