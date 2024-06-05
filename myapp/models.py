# myapp/models.py
from django.db import models
from django.utils import timezone

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
# myapp/models.py
from django.db import models
from django.utils import timezone

class FeatureProduct(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    initial_price = models.DecimalField(max_digits=10, decimal_places=2)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, editable=False)
    feature_image = models.ImageField(upload_to='feature_product_images/')
    sale_end_time = models.DateTimeField()

    def save(self, *args, **kwargs):
        # Calculate discount percent
        if self.initial_price > 0:
            self.discount_percent = ((self.initial_price - self.final_price) / self.initial_price) * 100
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
