# myapp/models.py
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    initial_rate = models.DecimalField(max_digits=10, decimal_places=2)
    final_rate = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='productsImage only')
    color = models.CharField(max_length=50)
    available = models.BooleanField(default=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.title
