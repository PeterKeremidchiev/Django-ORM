# Generated by Django 4.2.4 on 2023-10-28 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_hotelroom_room_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelroom',
            name='room_type',
            field=models.CharField(choices=[('St', 'Standart'), ('De', 'Deluxe'), ('Su', 'Suite')]),
        ),
    ]