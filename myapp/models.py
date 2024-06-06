# myapp/models.py
from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    initial_rate = models.DecimalField(max_digits=10, decimal_places=2)
    final_rate = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', default='path/to/default/image.jpg')
    color = models.CharField(max_length=50, default='default_color')
    available = models.BooleanField(default=True)
    stock = models.IntegerField(null=True)
    Category = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title
# myapp/models.py

class FeatureProduct(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    initial_price = models.DecimalField(max_digits=10, decimal_places=2)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, editable=False, default=0)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)  # New field for discount amount
    feature_image = models.ImageField(upload_to='feature_product_images/', default='feature_product_images/default_image.jpg')
    sale_end_time = models.DateTimeField()
    category = models.CharField(max_length=500, null=True, blank=True)  # Changed to lowercase "category"
    available = models.BooleanField(default=True)
    stock = models.IntegerField(null=True)
    color = models.CharField(max_length=50, default='default_color')

    def save(self, *args, **kwargs):
        if self.initial_price > 0:
            self.discount_percent = ((self.initial_price - self.final_price) / self.initial_price) * 100
            self.discount_amount = self.initial_price - self.final_price  # Calculate discount amount
        super(FeatureProduct, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class BestSellingProduct(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    initial_rate = models.DecimalField(max_digits=10, decimal_places=2)
    final_rate = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='best_selling_product_images/', default='best_selling_product_images/default_image.jpg')
    color = models.CharField(max_length=50, default='default_color')
    available = models.BooleanField(default=True)
    stock = models.IntegerField(null=True)
    Category = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title
    

class FlashSale(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    initial_price = models.DecimalField(max_digits=10, decimal_places=2)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='flash_sale_photos/', default='flash_sale_photos/default_photo.jpg')
    remaining_time = models.DateTimeField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    product_id = models.CharField(max_length=50)

    def time_remaining(self):
        now = timezone.now()
        remaining_time = self.remaining_time - now
        return remaining_time.total_seconds() // 3600, (remaining_time.total_seconds() // 60) % 60

    def __str__(self):
        return self.title



# models.py
