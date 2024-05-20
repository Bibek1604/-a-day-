from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price_in_npr = models.DecimalField(max_digits=10, decimal_places=2)
    total_product = models.PositiveIntegerField()
    available_product = models.PositiveIntegerField()
    offer_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    available_offer_start_date = models.DateField(null=True, blank=True)
    available_offer_end_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='product_photos/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:  # On initial creation
            self.available_product = self.total_product
        super().save(*args, **kwargs)

    def is_offer_valid(self):
        if self.offer_price and self.available_offer_start_date and self.available_offer_end_date:
            now = timezone.now().date()
            return self.available_offer_start_date <= now <= self.available_offer_end_date
        return False

    def __str__(self):
        return self.name

