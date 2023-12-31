import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


# Import your models
# Create and check models
# Run and print your queries
from main_app.models import Animal, Mammal, Bird, Reptile, Veterinarian, Employee, ZooKeeper, ZooDisplayAnimal
from datetime import date, timedelta




