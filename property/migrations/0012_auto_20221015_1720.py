# Generated by Django 3.2.16 on 2022-10-15 14:20
import phonenumbers

from django.db import migrations
from phonenumber_field.phonenumber import PhoneNumber

def get_normalized_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flat_set = Flat.objects.all()
    for flat in flat_set.iterator():
        raw_phone_number = flat.owners_phonenumber
        parsed_phone_number = phonenumbers.parse(raw_phone_number,"RU")
        if (parsed_phone_number.country_code==7 and
            len(str(parsed_phone_number.national_number==10)) and
            phonenumbers.is_valid_number(parsed_phone_number) and
            phonenumbers.is_possible_number(parsed_phone_number)) :
            flat.owners_pure_phone = PhoneNumber.from_string(phone_number=raw_phone_number,
                                                             region='RU').as_e164
        else:
            flat.owners_pure_phone = 'Не удалось получить номер'
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_flat_owners_pure_phone'),
    ]

    operations = [migrations.RunPython(get_normalized_phone_number),
    ]
