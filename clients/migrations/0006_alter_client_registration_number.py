# Generated by Django 5.0.6 on 2024-06-10 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_remove_client_days_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='registration_number',
            field=models.CharField(max_length=100),
        ),
    ]
