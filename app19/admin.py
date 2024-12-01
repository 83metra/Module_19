from django.contrib import admin

# Register your models here.

from .models import Blog_Post, News

# admin.site.register(Blog_Post)
admin.site.register(News)

@admin.register(Blog_Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created_at')
    list_filter = ['thema']
