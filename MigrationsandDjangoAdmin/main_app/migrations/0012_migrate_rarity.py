# Generated by Django 4.2.4 on 2023-10-24 17:32

from django.db import migrations

def set_rarity(apps, schema_editor):
    item_model = apps.get_model('main_app', 'Item')

    items = item_model.objects.all()

    for item in items:
        if item.price <= 10:
            item.rarity = "Rare"
        elif item.price <= 20:
            item.rarity = "Very Rare"
        elif item.price <= 30:
            item.rarity = "Extremely Rare"
        else:
            item.rarity = "Mega Rare"
    item_model.objects.bulk_update(items, ['rarity'])

def set_rarity_reverse(apps, schema_editor):
    item_model = apps.get_model('main_app', 'Item')

    item_rarity_default = item_model._meta.get_field('rarity').default

    for item in item_model.objects.all():
        item.rarity = item_rarity_default

    item_model.objects.bulk_update(item_model.objects.all(), ['rarity'])

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_item'),
    ]

    operations = [
        migrations.RunPython(set_rarity, reverse_code=set_rarity_reverse)
    ]