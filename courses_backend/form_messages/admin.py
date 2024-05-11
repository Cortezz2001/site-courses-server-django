from django.contrib import admin
from .models import FormMessage

class FormMessageAdmin(admin.ModelAdmin):
    readonly_fields = [f.name for f in FormMessage._meta.get_fields()]
    list_display = ['email', 'created_at']
    
    def created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')

    def has_add_permission(self, request):
        # Запрещаем добавление записей
        return False
    
    def has_change_permission(self, request, obj=None):
        # Запрещаем редактирование записей
        return False
    
    
admin.site.register(FormMessage, FormMessageAdmin)