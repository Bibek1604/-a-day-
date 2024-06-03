from django.db import models

# Create your models here.
# coupon/models.py
from django.db import models
from django.utils import timezone
from django.db import transaction

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    usage_count = models.PositiveIntegerField(default=0)
    max_usage = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='coupons')

    def __str__(self):
        return self.code

    def is_valid(self):
        return self.active and self.usage_count < self.max_usage and self.expires_at > timezone.now()

    def use_coupon(self):
        if self.is_valid():
            with transaction.atomic():
                coupon = Coupon.objects.select_for_update().get(pk=self.pk)
                if coupon.is_valid():
                    coupon.usage_count += 1
                    coupon.save()
                    return True
        return False
