# Generated by Django 4.2.4 on 2023-11-13 15:22

import django.core.validators
from django.db import migrations, models
import main_app.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[main_app.validators.validate_name])),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(18, message='Age must be greater than 18')])),
                ('email', models.EmailField(error_messages={'invalid': 'Enter a valid email address'}, max_length=254)),
                ('phone_number', models.CharField(max_length=13, validators=[main_app.validators.validate_phone_number])),
                ('website_url', models.URLField(error_messages={'invalid': 'Enter a valid URL'})),
            ],
        ),
    ]
