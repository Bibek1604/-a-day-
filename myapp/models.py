from django.db import models
from django.utils import timezone

# Define category choices
CATEGORY_CHOICES = [
    ('Newiphone', 'New iPhone'),
    ('OldIphone', 'Old iPhone'),
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
    ('Yellow', 'Yellow'),
    ('Slate', 'Slate'),
]


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    initial_rate = models.DecimalField(max_digits=10, decimal_places=2)
    final_rate = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    photo = models.ImageField(upload_to='product_images/', default='path/to/default/image.jpg')

    color = models.CharField(max_length=50, choices=COLOR_CHOICES, default='Red')
    available = models.BooleanField(default=True)
    stock = models.IntegerField(null=True)
    category = models.CharField(max_length=500, choices=CATEGORY_CHOICES, null=True, blank=True)
    warranty = models.CharField(max_length=100, null=True, blank=True)
    storage = models.CharField(max_length=100, null=False, blank=True)

    def __str__(self):
        return self.title

class FeatureProduct(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    initial_rate = models.DecimalField(max_digits=10, decimal_places=2)
    final_rate = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, editable=False, default=0)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    photo = models.ImageField(upload_to='feature_product_images/', default='feature_product_images/default_image.jpg')
    sale_end_time = models.DateTimeField()
    category = models.CharField(max_length=500, choices=CATEGORY_CHOICES, null=True, blank=True)
    available = models.BooleanField(default=True)
    stock = models.IntegerField(null=True)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, default='Red')
    warranty = models.CharField(max_length=100, null=True, blank=True)
    storage = models.CharField(max_length=100, null=False, blank=True)

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
    photo = models.ImageField(upload_to='best_selling_product_images/', default='best_selling_product_images/default_image.jpg')
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, default='Red')
    available = models.BooleanField(default=True)
    stock = models.IntegerField(null=True)
    category = models.CharField(max_length=500, choices=CATEGORY_CHOICES, null=True, blank=True)
    warranty = models.CharField(max_length=100, null=True, blank=True)
    storage = models.CharField(max_length=100, null=False, blank=True)

    def __str__(self):
        return self.title

class FlashSale(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    initial_rate = models.DecimalField(max_digits=10, decimal_places=2)
    final_rate = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='flash_sale_photos/', default='flash_sale_photos/default_photo.jpg')
    remaining_time = models.DateTimeField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    product_id = models.CharField(max_length=50)
    warranty = models.CharField(max_length=100, null=True, blank=True)
    storage = models.CharField(max_length=100, null=False, blank=True)

    def time_remaining(self):
        now = timezone.now()
        remaining_time = self.remaining_time - now
        if remaining_time.total_seconds() < 0:
            return 0, 0, 0, 0  # Sale has ended

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

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order {self.id} by {self.customer.name}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantity} x {self.product.title}'
