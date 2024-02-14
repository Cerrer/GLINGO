# Generated by Django 5.0 on 2024-02-05 15:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appKey', '0006_product_currency'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'подкатегорию', 'verbose_name_plural': 'подкатегории'},
        ),
        migrations.CreateModel(
            name='PhotoProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phote', models.ImageField(upload_to='product', verbose_name='Изображение')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appKey.product', verbose_name='Продукты')),
            ],
            options={
                'verbose_name': 'изображение',
                'verbose_name_plural': 'Изображение продуктов',
            },
        ),
    ]