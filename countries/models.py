from django.db import models

class Country(models.Model):
    ISO2 = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=100)
  
    class Meta:
        indexes = [
            models.Index(fields=['ISO2'], name='ISO2_idx'),
        ]

    def __str__(self):
        return self.name