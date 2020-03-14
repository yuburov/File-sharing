from django.db import models

from django.contrib.auth.models import User
from django.db import models


class File(models.Model):
    file = models.FileField(null= False, blank=False, upload_to='files', verbose_name='Фото')
    caption = models.CharField(max_length=200, null=False, blank=False, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='files', verbose_name='Автор')


    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'