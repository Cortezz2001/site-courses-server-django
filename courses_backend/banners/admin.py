from django.contrib import admin
from .models import (
    Banner
)
from django.utils.html import format_html

class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_img', 'created_at')

    def created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')
    def display_img(self, obj):
        return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format(obj.img))    
    display_img.short_description = 'Изображение'
admin.site.register(Banner, BannerAdmin)