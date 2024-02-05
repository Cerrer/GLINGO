from django.contrib import admin
from .models import Category, Product, Subcategory, PhotosProduct
from django_summernote.admin import SummernoteModelAdmin

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display =['id', 'title']
#     list_display_links =['title']

class PhotosProductStacet(admin.StackedInline):
    model = PhotosProduct
    extra = 0       # Дочерний

@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    inlines = [PhotosProductStacet]
    list_display =['id', 'title', 'price']
    list_display_links =['title']
    raw_id_fields = ['subcategory']
    summernote_fields = ('desc')
    class Meta:
        model = Product

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display =['id', 'category','title',]
    list_display_links =['title',]
    list_filter = ('category',)
    
class SubcategoryStaked(admin.StackedInline):     # Позволяет добавлять много раз
    model = Subcategory                           # Дочерний блок
    extra = 0                                     # Выводит кол-во полей
    search_fields = ['title']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryStaked]
    class Meta:
        model = Category                          # Родитель

