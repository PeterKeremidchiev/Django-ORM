# Generated by Django 4.2.4 on 2023-10-24 18:12

from django.db import migrations
from django.utils import timezone


def set_delivery_and_waranty(apps, schema_editor):
    order_model = apps.get_model("main_app", 'Order')

    for order in order_model.objects.all():
        if order.status == 'Pending':
            order.delivery = order.order_date + timezone.timedelta(days=3)
            order.save()
        elif order.status == "Completed":
            order.warranty = "24 months"
            order.save()
        elif order.status == "Canceled":
            order.delete()

def reverse_delivery_and_waranty(apps, schema_editor):
    order_model = apps.get_model("main_app", 'Order')

    for order in order_model.objects.all():
        if order.status == 'Pending':
            order.delivery = None

        elif order.status == "Completed":
            order.warranty = "No warranty"

        order.save()

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_order'),
    ]

    operations = [
        migrations.RunPython(set_delivery_and_waranty, reverse_code=reverse_delivery_and_waranty)
    ]
