from django.core.exceptions import ValidationError


def validate_menu_categories(value):
    categories = ["Appetizers", "Main Course", "Desserts"]
    for cat in categories:
        if cat not in value:
            raise ValidationError('The menu must include each of the categories "Appetizers", "Main Course", "Desserts".')