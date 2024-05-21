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

class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateField()
    valid_to = models.DateField()

    def is_valid(self):
        now = timezone.now().date()
        return self.valid_from <= now <= self.valid_to

    def __str__(self):
        return self.code

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    battery_health_condition = models.CharField(max_length=100)
    coupon_code = models.ForeignKey(Coupon, null=True, blank=True, on_delete=models.SET_NULL)

    def apply_discount(self):
        if self.coupon_code and self.coupon_code.is_valid():
            discount_amount = (self.price * self.coupon_code.discount_percent) / 100
            discounted_price = self.price - discount_amount
            return discounted_price
        return self.price

    def save(self, *args, **kwargs):
        if self.coupon_code and self.coupon_code.is_valid():
            self.price = self.apply_discount()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} in {self.category.name}"
