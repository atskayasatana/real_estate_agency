# Generated by Django 2.2.24 on 2022-11-11 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0028_auto_20221112_0129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='flats',
            new_name='flat',
        ),
    ]
