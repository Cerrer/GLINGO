from django.contrib import admin
from .models import ContentBanner

@admin.register(ContentBanner)
class ContentBannerAdmin(admin.ModelAdmin):
    pass