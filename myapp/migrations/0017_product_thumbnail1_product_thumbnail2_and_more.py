# Generated by Django 4.1.13 on 2024-06-07 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_alter_bestsellingproduct_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumbnail1',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail2',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail3',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to='product_images/'),
        ),
    ]