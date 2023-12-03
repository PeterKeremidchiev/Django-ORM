from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.managers import AuthorManager
from main_app.mixins import ContentMixin, PublishedMixin

# Create your models here.
CATEGORY_CHOICES = [
    ("Technology", "Technology"),
    ("Science", "Science"),
    ("Education", "Education"),
]
class Author(models.Model):
    full_name = models.CharField(max_length=100, validators=[MinLengthValidator(3), MaxLengthValidator(100)])
    email = models.EmailField(unique=True)
    is_banned = models.BooleanField(default=False)
    birth_year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2005)])
    website = models.URLField(null=True, blank=True)

    objects = AuthorManager()
class Article(PublishedMixin, ContentMixin, models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(5), MaxLengthValidator(200)])
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default="Technology")
    authors = models.ManyToManyField(Author, related_name="authors_articles")

class Review(PublishedMixin, ContentMixin, models.Model):
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author_reviews")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="article_reviews")
    asd = models.Ara

