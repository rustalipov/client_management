# Generated by Django 5.0.6 on 2024-06-11 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_alter_client_registration_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='client',
            name='inn',
            field=models.IntegerField(max_length=14),
        ),
        migrations.AlterField(
            model_name='client',
            name='registration_number',
            field=models.IntegerField(max_length=100),
        ),
    ]
