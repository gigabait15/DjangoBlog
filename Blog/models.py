from django.db import models
from config.settings import NULLABLE


class Posts(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    image = models.ImageField(upload_to="blog/", **NULLABLE, verbose_name="изображение")
    count_views = models.PositiveIntegerField(default=0, verbose_name="количество просмотров")
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='дата и время публикации')

    author = models.ForeignKey('User.Users', on_delete=models.PROTECT, verbose_name='автор публикации')
    comment = models.ForeignKey('Comment.Comments', on_delete=models.CASCADE, verbose_name='комментарии')

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-date_create']

    def __str__(self):
        return self.title


