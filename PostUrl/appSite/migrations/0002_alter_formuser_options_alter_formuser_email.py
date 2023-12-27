# Generated by Django 5.0 on 2023-12-27 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSite', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formuser',
            options={'verbose_name': ('Контактную информацию',), 'verbose_name_plural': 'Контактаня информация.'},
        ),
        migrations.AlterField(
            model_name='formuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Почта'),
        ),
    ]
