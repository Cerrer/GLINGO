from django.db import models

class FormUser(models.Model):
    name = models.CharField(
        verbose_name = "Имя",
        null=False,
        max_length=40,
        default="Неизвестно"
    )
    email = models.EmailField(
        verbose_name="Почта",
        null=False,
        unique=True,               # unique - уникальное поле
        db_index=True              # db_index - фильтрация и поиск в базе данных
    )
    age = models.IntegerField(
        verbose_name="Возраст",
        null=False
    )
    def __str__(self):
        return self.email
    class Meta:
        verbose_name="Контактную информацию",
        verbose_name_plural="Контактаня информация."
