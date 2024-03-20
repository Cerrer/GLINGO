from django.db import models

class ProductShop(models.Model):
    title = models.CharField('Имя товара', null=False, max_length=150)
    count = models.IntegerField('Кол-во товаров наскладе', null=False, default=0)
    price = models.FloatField('Цена товаров', null=False, default=0)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
