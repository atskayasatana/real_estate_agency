# Generated by Django 4.1.3 on 2022-11-21 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0032_remove_owner_owners_phonenumber_owner_phone'),
    ]

    operations = [
        migrations.RenameField('owner', 'owner', 'name')
    ]
