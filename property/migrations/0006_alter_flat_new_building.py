# Generated by Django 3.2.16 on 2022-10-14 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_auto_20221014_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(choices=[(True, 'Да'), (False, 'Нет'), (None, 'Неизвестно')], default=None, verbose_name='Новостройка'),
        ),
    ]
