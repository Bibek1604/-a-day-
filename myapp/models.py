from django.db import models
from django.utils import timezone

# Define category choices
CATEGORY_CHOICES = [
    ('NewiPhone', 'New iPhone'),
    ('OldiPhone', 'Old iPhone'),
    ('Cover', 'Cover'),
    ('Electronics', 'Electronics'),
    ('NewAndroid', 'New Android'),
    ('UsedAndroid', 'Used Android'),
    ('Laptop', 'Laptop'),
    ('Earbuds', 'Earbuds'),
    ('Android', 'Android'),
]

# Define color choices
COLOR_CHOICES = [
    ('Red', 'Red'),
    ('Black', 'Black'),
    ('White', 'White'),
    ('Purple', 'Purple'),
    ('Blue', 'Blue'),
    ('Green', 'Green'),
    ('Yellow', 'Yellow'),
    ('Pink', 'Pink'),
    ('Coral', 'Coral'),
    ('Space Gray', 'Space Gray'),
    ('Silver', 'Silver'),
    ('Gold', 'Gold'),
    ('Rose Gold', 'Rose Gold'),
    ('Midnight', 'Midnight'),
    ('Starlight', 'Starlight'),
    ('Jet Black', 'Jet Black'),
    ('Graphite', 'Graphite'),
    ('Pacific Blue', 'Pacific Blue'),
    ('Midnight Green', 'Midnight Green'),
    ('Sierra Blue', 'Sierra Blue'),
    ('Alpine Green', 'Alpine Green'),
    ('Deep Purple', 'Deep Purple'),
    ('Slate', 'Slate'),
]

class Product(models.Model):
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    initial_rate = models.DecimalField(max_digits=10, decimal_places=2)
    final_rate = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    pic = models.ImageField(upload_to='product_images/', default='path/to/default/image.jpg')
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, default='Red')
    available = models.BooleanField(default=True)
    stock = models.IntegerField(null=True)
    category = models.CharField(max_length=500, choices=CATEGORY_CHOICES, null=True, blank=True)
    warranty = models.CharField(max_length=100, null=True, blank=True)
    storage = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

class FeatureProduct(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    initial_rate = models.DecimalField(max_digits=10, decimal_places=2)
    final_rate = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, editable=False, default=0)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    pic = models.ImageField(upload_to='feature_product_images/', default='feature_product_images/default_image.jpg')
    sale_end_time = models.DateTimeField()
    category = models.CharField(max_length=500, choices=CATEGORY_CHOICES, null=True, blank=True)
    available = models.BooleanField(default=True)
    stock = models.IntegerField(null=True)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, default='Red')
    warranty = models.CharField(max_length=100, null=True, blank=True)
    storage = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if self.initial_rate > 0:
            self.discount_percent = ((self.initial_rate - self.final_rate) / self.initial_rate) * 100
            self.discount_amount = self.initial_rate - self.final_rate
        super(FeatureProduct, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class BestSellingProduct(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    initial_rate = models.DecimalField(max_digits=10, decimal_places=2)
    final_rate = models.DecimalField(max_digits=10, decimal_places=2)
    pic = models.ImageField(upload_to='best_selling_product_images/', default='best_selling_product_images/default_image.jpg')
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, default='Red')
    available = models.BooleanField(default=True)
    stock = models.IntegerField(null=True)
    category = models.CharField(max_length=500, choices=CATEGORY_CHOICES, null=True, blank=True)
    warranty = models.CharField(max_length=100, null=True, blank=True)
    storage = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

class FlashSale(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    initial_rate = models.DecimalField(max_digits=10, decimal_places=2)
    final_rate = models.DecimalField(max_digits=10, decimal_places=2)
    pic = models.ImageField(upload_to='flash_sale_photos/', default='flash_sale_photos/default_photo.jpg')
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    warranty = models.CharField(max_length=100, null=True, blank=True)
    storage = models.CharField(max_length=100, blank=True)

    def time_remaining(self):
        now = timezone.now()
        remaining_time = self.remaining_time - now
        if remaining_time.total_seconds() < 0:
            return 0, 0, 0, 0  

        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return days, hours, minutes, seconds
    def __str__(self):
        return self.title  

class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code

    def is_valid(self):
        now = timezone.now()
        return self.is_active and self.start_date <= now <= self.end_date

class Code(models.Model):
    promodis = models.CharField(max_length=255)

    def __str__(self):
        return self.promodis

class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address_line = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    PAY_WITH_CASH = 'cash'
    PAY_WITH_DELIVERY = 'delivery'
    PAYMENT_CHOICES = [
        (PAY_WITH_CASH, 'Pay with Cash'),
        (PAY_WITH_DELIVERY, 'Pay with Delivery')
    ]
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES)

    products = models.JSONField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)  # To track order time

    def __str__(self):
        return f"Order {self.id} by {self.first_name} {self.last_name}"