from django.db import models

class ContentNews(models.Model):
    title = models.CharField(
        verbose_name="Заголовок новости",
        max_length=200,
        null=False
    )
    name_url = models.CharField(
        verbose_name="Имя ссылки",
        max_length=200,
        null=False
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name ='Новость'
        verbose_name_plural ='Новости'