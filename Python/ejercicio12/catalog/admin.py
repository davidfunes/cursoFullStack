from django.contrib import admin

from .models import Director, Film


class filmAdmin(admin.ModelAdmin):
    fields = ['year', 'title', 'sinopsis', 'director']

admin.site.register(Director)
admin.site.register(Film, filmAdmin)