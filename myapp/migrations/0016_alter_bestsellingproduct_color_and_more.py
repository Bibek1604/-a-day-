# Generated by Django 4.1.13 on 2024-06-07 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_rename_storage_bestsellingproduct_storage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestsellingproduct',
            name='color',
            field=models.CharField(choices=[('Red', 'Red'), ('Black', 'Black'), ('White', 'White'), ('Purple', 'Purple'), ('Blue', 'Blue'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Pink', 'Pink'), ('Coral', 'Coral'), ('Space Gray', 'Space Gray'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Rose Gold', 'Rose Gold'), ('Midnight', 'Midnight'), ('Starlight', 'Starlight'), ('Jet Black', 'Jet Black'), ('Graphite', 'Graphite'), ('Pacific Blue', 'Pacific Blue'), ('Midnight Green', 'Midnight Green'), ('Sierra Blue', 'Sierra Blue'), ('Alpine Green', 'Alpine Green'), ('Deep Purple', 'Deep Purple'), ('Yellow', 'Yellow'), ('Slate', 'Slate')], default='Red', max_length=50),
        ),
        migrations.AlterField(
            model_name='featureproduct',
            name='color',
            field=models.CharField(choices=[('Red', 'Red'), ('Black', 'Black'), ('White', 'White'), ('Purple', 'Purple'), ('Blue', 'Blue'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Pink', 'Pink'), ('Coral', 'Coral'), ('Space Gray', 'Space Gray'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Rose Gold', 'Rose Gold'), ('Midnight', 'Midnight'), ('Starlight', 'Starlight'), ('Jet Black', 'Jet Black'), ('Graphite', 'Graphite'), ('Pacific Blue', 'Pacific Blue'), ('Midnight Green', 'Midnight Green'), ('Sierra Blue', 'Sierra Blue'), ('Alpine Green', 'Alpine Green'), ('Deep Purple', 'Deep Purple'), ('Yellow', 'Yellow'), ('Slate', 'Slate')], default='Red', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('Red', 'Red'), ('Black', 'Black'), ('White', 'White'), ('Purple', 'Purple'), ('Blue', 'Blue'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Pink', 'Pink'), ('Coral', 'Coral'), ('Space Gray', 'Space Gray'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Rose Gold', 'Rose Gold'), ('Midnight', 'Midnight'), ('Starlight', 'Starlight'), ('Jet Black', 'Jet Black'), ('Graphite', 'Graphite'), ('Pacific Blue', 'Pacific Blue'), ('Midnight Green', 'Midnight Green'), ('Sierra Blue', 'Sierra Blue'), ('Alpine Green', 'Alpine Green'), ('Deep Purple', 'Deep Purple'), ('Yellow', 'Yellow'), ('Slate', 'Slate')], default='Red', max_length=50),
        ),
    ]