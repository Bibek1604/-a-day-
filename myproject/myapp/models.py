from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    photo = models.ImageField(upload_to='product_photos/', null=True, blank=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price_in_npr = models.DecimalField(max_digits=10, decimal_places=2)
    total_product = models.PositiveIntegerField()
    available_product = models.PositiveIntegerField()
    offer_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    available_offer_start_date = models.DateField(null=True, blank=True)
    available_offer_end_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # If it's a new product being added
            self.available_product = self.total_product
        else:
            previous_product = Product.objects.get(pk=self.pk)
            previous_purchase = previous_product.total_product - previous_product.available_product
            current_purchase = self.total_product - self.available_product
            self.available_product = previous_product.available_product - previous_purchase + current_purchase
        super().save(*args, **kwargs)

    def is_offer_valid(self):
        if self.offer_price and self.available_offer_start_date and self.available_offer_end_date:
            now = timezone.now().date()
            return self.available_offer_start_date <= now <= self.available_offer_end_date
        return False

    def __str__(self):
        return self.name
