
from django.contrib.auth.models import User
from django.db import models

GENERAL = 'general'
HIDDEN = 'hidden'
PRIVATE = 'private'

GENEREAL_ACCESS_CHOICES = (
    (GENERAL, 'Общий'),
    (HIDDEN, 'Скрытый'),
    (PRIVATE, 'Приватный'),
)

class File(models.Model):
    file = models.FileField(null= False, blank=False, upload_to='files', verbose_name='Фото')
    caption = models.CharField(max_length=200, null=False, blank=False, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='files', verbose_name='Автор')
    general_access = models.CharField(max_length=50, choices=GENEREAL_ACCESS_CHOICES, default=GENERAL, verbose_name='Общий доступ')
    private_users = models.ManyToManyField(User, related_name='access_files', verbose_name='Приват')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'