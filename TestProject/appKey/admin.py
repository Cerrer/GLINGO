from django.contrib import admin
from .models import Category, Product, Subcategory

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display =['id', 'title']
#     list_display_links =['title']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =['id', 'title', 'price']
    list_display_links =['title']

# @admin.register(Subcategory)
# class SubcategoryAdmin(admin.ModelAdmin):
#     list_display =['id', 'category','title',]
#     list_display_links =['title',]
#     list_filter = ('category',)
    
class SubcategoryStaked(admin.StackedInline):     # Позволяет добавлять много раз
    model = Subcategory                           # Дочерний блок
    extra = 0                                     # Выводит кол-во полей

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryStaked]
    class Meta:
        model = Category                          # Дочерний блок

