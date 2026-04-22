from django.contrib import admin

# Register your models here.
from . import models


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'status', 'publish', 'author']

admin.site.register(models.Post, AuthorAdmin)
