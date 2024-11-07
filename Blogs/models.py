from django.db import models
from config.settings import NULLABLE


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    number_of_views = models.IntegerField(
        default=0, verbose_name="количество просмотров"
    )
    image = models.ImageField(upload_to="blog/", verbose_name="изображение", **NULLABLE)
    tags = models.TextField(**NULLABLE, verbose_name='tags')


    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title
