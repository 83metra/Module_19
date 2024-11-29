from django.contrib import admin
from .models import Blog_Post
# from .models import Post

# Register your models here.
# admin.site.register(Post)

@admin.register(Blog_Post)
class Blog_PostAdmin(admin.ModelAdmin):
    list_display = ('title',) # поля для отображения в списке
    search_fields = ('title',) # поля для поиска
    list_filter = ('teg', 'title')

    fieldsets = (
        (None, {
            'fields': ('title', 'text')
        }),
        ('Дополнительные настройки', {
            'classes': ('collapse',), # скрытие секции по умолчанию
            'fields': ('teg',)
        })
    )