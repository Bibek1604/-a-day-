# Generated by Django 4.1.13 on 2024-06-26 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_notification_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
