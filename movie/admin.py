from django.contrib import admin
from .models import Movie

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'genre', 'time']
    list_editable = ['genre', 'time']
    list_filter = ['genre']
    search_fields = ['name', 'user']
    ordering = ['name']