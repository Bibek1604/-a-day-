# Generated by Django 4.1.13 on 2024-06-15 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_delete_timerecord_flashsale_days_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.PositiveIntegerField(default=0)),
                ('hours', models.PositiveIntegerField(default=0)),
                ('minutes', models.PositiveIntegerField(default=0)),
                ('seconds', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='flashsale',
            name='days',
        ),
        migrations.RemoveField(
            model_name='flashsale',
            name='hours',
        ),
        migrations.RemoveField(
            model_name='flashsale',
            name='minutes',
        ),
        migrations.RemoveField(
            model_name='flashsale',
            name='seconds',
        ),
    ]

