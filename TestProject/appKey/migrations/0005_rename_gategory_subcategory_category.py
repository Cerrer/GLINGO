# Generated by Django 5.0 on 2024-01-31 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appKey', '0004_remove_product_category_product_subcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='gategory',
            new_name='category',
        ),
    ]
