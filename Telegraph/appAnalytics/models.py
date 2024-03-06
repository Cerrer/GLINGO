from django.db import models
from appPublication.models import PubNews

class StaticLink(models.Model):
    pub_news = models.ForeignKey(
        PubNews,
        on_delete=models.CASCADE,
        null=False,
        verbose_name="Публикация"
    )
    os = models.CharField(
        verbose_name="Операционная система",
        null=True,
        blank=True,
        max_length=150
    )
    browser = models.CharField(
        verbose_name="Браузер",
        null=True,
        blank=True,
        max_length=150
    )
    type_device = models.CharField(
        verbose_name="Тип устройство",
        choices=[
            ('mobile', 'Теьефон'),
            ('table', 'Планшет'),
            ('pc', 'ПК')
        ],
        null=False,
        max_length=150
    )
    bot = models.BooleanField(
        verbose_name="Определяет бота",
        choices=[
            (True, 'Да'),
            (False, 'Нет')
        ],
        default=False,
        null=True,
        blank=True
    )
    touch_capable = models.BooleanField(
        verbose_name="Поддержка сенсорного экрана",
        choices=[
            (True, 'Да'),
            (False, 'Нет')
        ],
        default=False,
        null=True,
        blank=True
    )
    email_client = models.BooleanField(
        verbose_name="email",
        choices=[
            (True, 'Да'),
            (False, 'Нет')
        ],
        default=False,
        null=True,
        blank=True
    )
    def __str__(self):
        return self.pub_news.name_url
    class Meta:
        verbose_name="историю"
        verbose_name_plural="Просмотры"