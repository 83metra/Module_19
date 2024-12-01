from django.db import models

# Create your models here.

class Blog_Post(models.Model):
    # id = models.IntegerField(primary_key=True, default=True, verbose_name='Номер поста', )
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    text = models.TextField(max_length=1000,verbose_name='Пост')
    thema = models.CharField(max_length=20, verbose_name='Тема')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    # category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at'] # сортировка по дате создания в обратном порядке