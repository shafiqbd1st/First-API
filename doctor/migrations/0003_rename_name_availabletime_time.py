# Generated by Django 5.0.3 on 2024-04-25 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_alter_doctor_fee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='availabletime',
            old_name='name',
            new_name='time',
        ),
    ]
