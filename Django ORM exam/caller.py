import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from django.db.models import Q, Count, F, Avg, Max, Sum
from main_app.models import Author, Article, Review


# Create and run your queries within functions

def get_authors(search_name=None, search_email=None):
    if search_name is None and search_email is None:
        return ""

    query = Q()
    query_full_name = Q(full_name__icontains=search_name)
    query_email = Q(email__icontains=search_email)

    if search_name and search_email:
        query = query_email & query_full_name
    elif search_name is not None:
        query = query_full_name
    else:
        query = query_email

    authors = Author.objects.filter(query).order_by("-full_name")
    if not authors:
        return ""

    result = []
    for author in authors:
        status = "Banned" if author.is_banned else "Not Banned"
        result.append(f"Author: {author.full_name}, email: {author.email}, status: {status}")
    return "\n".join(result)


def get_top_publisher():
    top_publisher = Author.objects.get_authors_by_article_count().filter(num_of_articles__gt=0).first()

    if not top_publisher:
        return ""

    return f"Top Author: {top_publisher.full_name} with {top_publisher.num_of_articles} published articles."


def get_top_reviewer():
    reviewer = (
        Author.objects.annotate(num_of_reviews=Count('author_reviews')).filter(num_of_reviews__gt=0).order_by(
            '-num_of_reviews', 'email').first())

    if not reviewer:
        return ""

    return f"Top Reviewer: {reviewer.full_name} with {reviewer.num_of_reviews} published reviews."


def get_latest_article():
    articles = (Article.objects
                .annotate(num_reviews=Count("article_reviews"), sum_ratings=Sum("article_reviews__rating"),
                          total_reviews=Count("article_reviews"))
                .last())

    if articles is None:
        return ""

    if articles.total_reviews == 0:
        avg_reviews_rating = 0
    else:
        avg_reviews_rating = articles.sum_ratings / articles.total_reviews

    authors = [author.full_name for author in articles.authors.all().order_by("full_name")]

    return (f"The latest article is: {articles.title}."
            f" Authors: {', '.join(authors)}."
            f" Reviewed: {articles.num_reviews} times."
            f" Average Rating: {avg_reviews_rating:.2f}.")


def get_top_rated_article():
    # top_article = (Article.objects
    #                .annotate(rating=Count("article_reviews__rating"), num_reviews=Count("article_reviews"))
    #                .order_by("-rating", "title").first())
    if Review.objects.all().count() is None:
        return ""
    top_article = Review.objects.annotate(top_rating=Max("rating")).order_by("-top_rating", "article__title").first()

    reviews = Review.objects.filter(article=top_article.article).aggregate(avg_rating=Avg('rating'))
    num_reviews = Review.objects.filter(article=top_article.article).count()
    if num_reviews == 0:
        return ""
    # avg_rating = Article.objects.aggregate(avg_rating=Avg('article_reviews__rating'))

    return (f"The top-rated article is: {top_article.article.title},"
            f" with an average rating of {reviews['avg_rating']:.2f},"
            f" reviewed {num_reviews} times.")


def ban_author(email=None):
    if email is None:
        return "No authors banned."

    query = Q(email__exact=email)
    author = Author.objects.annotate(num_of_reviews=Count("author_reviews")).filter(query)

    if not author:
        return "No authors banned."

    result = []
    for auth in author:
        auth.is_banned = True
        result.append(f"Author: {auth.full_name} is banned! {auth.num_of_reviews} reviews deleted.")
        auth.author_reviews.all().delete()
        auth.save()

    return "\n".join(result)

print(get_latest_article())