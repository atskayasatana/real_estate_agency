# Generated by Django 3.2.16 on 2022-10-14 20:47

from django.db import migrations

def get_type_of_building(apps, schema_editor):
    flat = apps.get_model('property','Flat')
    flat.objects.filter(construction_year__gte=2015).update(new_building=True)
    flat.objects.filter(construction_year__lt=2015).update(new_building=False)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_alter_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(get_type_of_building)
    ]
