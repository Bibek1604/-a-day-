# Generated by Django 5.0.6 on 2024-06-06 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_customer_order_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bestsellingproduct',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Category',
            new_name='category',
        ),
    ]