# Generated by Django 5.0.6 on 2024-06-05 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_bestsellingproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlashSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('initial_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('photo', models.ImageField(default='flash_sale_photos/default_photo.jpg', upload_to='flash_sale_photos/')),
                ('remaining_time', models.DateTimeField()),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('product_id', models.CharField(max_length=50)),
            ],
        ),
    ]