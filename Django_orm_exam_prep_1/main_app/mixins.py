from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class RepeatingFieldsMixin(models.Model):
    full_name = models.CharField(max_length=120, validators=[MinLengthValidator(2), MaxLengthValidator(120)])
    birth_date = models.DateField(default='1900-01-01')
    nationality = models.CharField(max_length=50, validators=[MaxLengthValidator(50)], default='Unknown')

    def __str__(self):
        return self.full_name

    class Meta:
        abstract = True

class TimeStampMixin(models.Model):
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class IsAwardedMixin(models.Model):
    is_awarded = models.BooleanField(default=False)

    class Meta:
        abstract = True