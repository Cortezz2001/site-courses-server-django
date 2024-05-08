from django.contrib import admin
from .models import (
    Event
)

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'format', 'img', 'created_at')
    search_fields = ('title', 'format')
    filter_horizontal = ('active_mentors',)
    # prepopulated_fields = {'slug': ('name',)}

    def created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')


admin.site.register(Event, EventAdmin)
