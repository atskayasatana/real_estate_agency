# Generated by Django 3.2.16 on 2022-10-15 13:03

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_flat_liked_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owners_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region=None),
        ),
    ]
