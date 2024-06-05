# Generated by Django 5.0.6 on 2024-06-05 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_category_featureproduct_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestSellingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('initial_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('final_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(default='best_selling_product_images/default_image.jpg', upload_to='best_selling_product_images/')),
                ('color', models.CharField(default='default_color', max_length=50)),
                ('available', models.BooleanField(default=True)),
                ('stock', models.IntegerField(null=True)),
                ('Category', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
