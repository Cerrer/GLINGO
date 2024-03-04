from django.db import models
from tinymce.models import HTMLField
import datetime
import uuid

# class Articless(models.Model):
#     title = models.CharField(max_length=300, null=True, blank=True)
#     content = HTMLField()
#     def __str__(self):
#         return self.title

class PubNews(models.Model):
    content = HTMLField(
        verbose_name="Содержание",
        null=False
    )
    date_time = models.DateTimeField(
        verbose_name="Дата и время публикации",
        null=False,
        default=datetime.datetime.now
    )
    name_url = models.CharField(
        verbose_name="Имя ссылки",
        max_length=20,
        null=False,
    )
    def __str__(self):
        return self.name_url
    class Meta:
        verbose_name = "публикацию"
        verbose_name_plural = "Публикации"