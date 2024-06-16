# Generated by Django 4.1.13 on 2024-06-15 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_rename_photo_bestsellingproduct_pic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.PositiveIntegerField(default=0)),
                ('hours', models.PositiveIntegerField(default=0)),
                ('minutes', models.PositiveIntegerField(default=0)),
                ('discount_percent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('warranty', models.CharField(blank=True, max_length=100, null=True)),
                ('storage', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='flashsale',
            name='discount_percent',
        ),
        migrations.RemoveField(
            model_name='flashsale',
            name='remaining_time',
        ),
        migrations.RemoveField(
            model_name='flashsale',
            name='storage',
        ),
        migrations.RemoveField(
            model_name='flashsale',
            name='warranty',
        ),
    ]