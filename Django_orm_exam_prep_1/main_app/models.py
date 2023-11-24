from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.managers import DirectorManager
from main_app.mixins import RepeatingFieldsMixin, TimeStampMixin, IsAwardedMixin

# Create your models here.

GENRE_CHOICES = (
    ('Action', 'Action'),
    ('Comedy', 'Comedy'),
    ('Drama', 'Drama'),
    ('Other', 'Other')
)

class Director(RepeatingFieldsMixin, models.Model):
    years_of_experience = models.SmallIntegerField(validators=[MinValueValidator(0)], default=0)

    objects = DirectorManager()

class Actor(RepeatingFieldsMixin, TimeStampMixin, IsAwardedMixin):
    pass

class Movie(TimeStampMixin, IsAwardedMixin, models.Model):

    title = models.CharField(max_length=150, validators=[MinLengthValidator(5), MaxLengthValidator(150)])
    release_date = models.DateField()
    storyline = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=6, choices=GENRE_CHOICES, validators=[MaxLengthValidator(6)], default='Other')
    rating = models.DecimalField(max_digits=3,
                                 decimal_places=1,
                                 validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], default=0.0)
    is_classic = models.BooleanField(default=False)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='director_movies')
    starring_actor = models.ForeignKey(Actor, null=True, blank=True, on_delete=models.SET_NULL, related_name='starring_movies')
    actors = models.ManyToManyField(Actor, related_name='actor_movies')

    def __str__(self):
        return self.title
