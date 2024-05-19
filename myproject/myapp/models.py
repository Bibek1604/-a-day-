from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name =models.CharField(max_length=100)
    category_id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.category_name
    
class Product(models.Model):
        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        name = models.CharField(max_length=100)
        picture = models.ImageField(upload_to='product_pictures/')
        description = models.TextField()
        price_in_npr = models.DecimalField(max_digits=10, decimal_places=2)
        
        def __str__(self):
            return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    seat = models.ForeignKey('Seat', on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - {self.seat.seat_number}"

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.seat_number
