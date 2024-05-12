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


