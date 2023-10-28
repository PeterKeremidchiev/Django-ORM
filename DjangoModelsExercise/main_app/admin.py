from django.contrib import admin

from main_app.models import Book


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'price', 'rating', 'description']
    list_filter = ['genre']
    search_fields = ['title']

    