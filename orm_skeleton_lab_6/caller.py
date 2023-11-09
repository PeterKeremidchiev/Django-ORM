import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Lecturer, Subject, Student, LecturerProfile

# Import your models
# Create and check models
# Run and print your queries

