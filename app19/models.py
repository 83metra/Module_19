from django.db import models

# Create your models here.

class Blog_Post(models.Model):
    # id = models.IntegerField(primary_key=True, default=True, verbose_name='Номер поста', )
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    text = models.TextField(max_length=1000,verbose_name='Пост')
    teg = models.CharField(max_length=20, verbose_name='Метка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


# class Post(models.Model):
#     title = models.CharField(max_length=50)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)