# Generated by Django 4.1.13 on 2024-06-06 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_rename_category_bestsellingproduct_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestsellingproduct',
            name='warrenty',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='featureproduct',
            name='warrenty',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='flashsale',
            name='warrenty',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='warrenty',
            field=models.IntegerField(null=True),
        ),
    ]
