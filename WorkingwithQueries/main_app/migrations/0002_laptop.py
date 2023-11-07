# Generated by Django 4.2.4 on 2023-10-31 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('As', 'Asus'), ('Ac', 'Acer'), ('Ap', 'Apple'), ('Le', 'Lenovo'), ('De', 'Dell')], max_length=100)),
                ('processor', models.CharField(max_length=100)),
                ('memory', models.PositiveIntegerField(help_text='Memory in GB')),
                ('storage', models.PositiveIntegerField(help_text='Storage in GB')),
                ('operation_system', models.CharField(choices=[('Win', 'Windows'), ('Mac', 'MacOS'), ('Lin', 'Linux'), ('Chr', 'Chrome OS')], max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
