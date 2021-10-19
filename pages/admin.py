from django.contrib import admin
from django.utils.html import format_html

from .models import Team


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(f'<img src="{object.photo.url}" width="40" style="border-radius: 50%;"/>')

    thumbnail.short_description = "Photo"
    list_display = ('id', 'thumbnail', 'first_name', 'desgination', 'created_date')
    list_display_links = ('id', 'thumbnail', 'first_name',)
    search_fields = ('first_name', 'last_name', 'desgination')
    list_filter = ('desgination',)

# Register your models here.
admin.site.register(Team, TeamAdmin)