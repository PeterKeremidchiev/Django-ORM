import os

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from django.db.models import Q, Count, Avg, F
from main_app.models import Director, Actor, Movie


# Create and run your queries within functions
def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ""

    query = Q()
    query_full_name = Q(full_name__icontains=search_name)
    query_nationality = Q(nationality__icontains=search_nationality)

    if search_name is not None and search_nationality is not None:
        query = query_full_name & query_nationality

    elif search_name is not None:
        query = query_full_name

    else:
        query = query_nationality

    directors = Director.objects.filter(query).order_by('full_name')

    if not directors:
        return ""

    result = []
    for director in directors:
        result.append(
            f"Director: {director.full_name}, nationality: {director.nationality}, experience: {director.years_of_experience}")

    return '\n'.join(result)


def get_top_director():
    top_director = Director.objects.get_directors_by_movies_count().first()
    if not top_director:
        return ""

    return f"Top Director: {top_director.full_name}, movies: {top_director.num_of_movies}."


def get_top_actor():
    top_actor = Actor.objects.prefetch_related('starring_movies') \
        .annotate(
        num_of_movies=Count('starring_movies'),
        movies_avg_rating=Avg('starring_movies__rating')) \
        .order_by('-num_of_movies', 'full_name') \
        .first()

    if not top_actor or not top_actor.num_of_movies:
        return ""

    movies = ", ".join(movie.title for movie in top_actor.starring_movies.all() if movie)

    return f"Top Actor: {top_actor.full_name}, " \
           f"starring in movies: {movies}, " \
           f"movies average rating: {top_actor.movies_avg_rating:.1f}"


def get_actors_by_movies_count():
    top_actors = Actor.objects.annotate(num_of_movies=Count('actor_movies')) \
                     .order_by('-num_of_movies', 'full_name')[:3]

    if not top_actors or not top_actors[0].num_of_movies:
        return ""

    result = []

    for actor in top_actors:
        result.append(f"{actor.full_name}, participated in {actor.num_of_movies} movies")

    return '\n'.join(result)


def get_top_rated_awarded_movie():
    movie = Movie.objects\
             .filter(is_awarded=True)\
             .order_by('-rating', 'title').first()

    if movie is None:
        return ""

    starring_actor = movie.starring_actor.full_name if movie.starring_actor else "N/A"
    cast = ', '.join([actors.full_name for actors in movie.actors.order_by('full_name')])

    return f"Top rated awarded movie: {movie.title}, " \
           f"rating: {movie.rating}. Starring actor: {starring_actor}. Cast: {cast}."


def increase_rating():
    movies = Movie.objects.filter(is_classic=True).filter(rating__lt=10.0)

    if not movies:
        return "No ratings increased."

    num_of_updated_movies = movies.update(rating=F('rating') + 0.1)

    return f"Rating increased for {num_of_updated_movies} movies."

# print(increase_rating())
