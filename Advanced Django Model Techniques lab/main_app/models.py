from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.validators import validate_menu_categories


# Create you
# r models here.

class ReviewMixin(models.Model):
    reviewer_name = models.CharField(max_length=100)
    review_content = models.TextField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])

    class Meta:
        abstract = True
        ordering = ["-rating"]


class Restaurant(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2, message="Name must be at least 2 characters long."),
                    MaxLengthValidator(100, message="Name cannot exceed 100 characters.")])
    location = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(2, message="Location must be at least 2 characters long."),
            MaxLengthValidator(200, message="Location cannot exceed 100 characters.")])
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[
            MinValueValidator(0, message="Rating must be at least 0.00."),
            MaxValueValidator(5, message="Rating cannot exceed 5.00.")])

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(validators=[validate_menu_categories])
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class RestaurantReview(ReviewMixin, models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta(ReviewMixin.Meta):
        verbose_name = "Restaurant Review"
        verbose_name_plural = "Restaurant Reviews"
        unique_together = ["reviewer_name", "restaurant"]
        abstract = True


class RegularRestaurantReview(RestaurantReview):
    pass

class FoodCriticRestaurantReview(RestaurantReview):
    food_critic_cuisine_area = models.CharField()

    class Meta(RestaurantReview.Meta):
        verbose_name = "Food Critic Review"
        verbose_name_plural = "Food Critic Reviews"


class MenuReview(ReviewMixin, models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta(ReviewMixin.Meta):
        verbose_name = "Menu Review"
        verbose_name_plural = "Menu Reviews"
        unique_together = ["reviewer_name", "menu"]
        indexes = [models.Index(fields=["menu"], name="main_app_menu_review_menu_id")]