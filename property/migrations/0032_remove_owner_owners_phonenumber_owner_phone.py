# Generated by Django 4.1.3 on 2022-11-18 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0031_alter_complaint_flat_alter_complaint_user_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="owner",
            name="owners_phonenumber",
        ),
        migrations.AddField(
            model_name="owner",
            name="phone",
            field=models.CharField(
                default="", max_length=10, verbose_name="Номер владельца"
            ),
        ),
    ]
