from django.db import models
from django.core.exceptions import ValidationError
import datetime

class ContentBanner(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=100,
        null=False
    )
    desc = models.TextField(
        verbose_name="Описание",
        null=False
    )
    number = models.IntegerField(
        verbose_name="Порядковый номер",
        null=True,
        blank=True
    )
    def clean(self):              #класс - Чистка
        super().clean()                   #метод -  чистка
        if ContentBanner.objects.count() > 3 and not self.pk:
            raise ValidationError("Вы превысили лимит записей. Всего доступно")
