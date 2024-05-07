from django.contrib import admin
from .models import (
    Event,
    Mentor,
)

class MentorInline(admin.TabularInline):
    model = Mentor
    extra = 1


class CourseInline(admin.TabularInline):
    model = Event
    extra = 1

class EventAdmin(admin.ModelAdmin):
    inlines = [
        MentorInline,
    ]
    list_display = ('id', 'title', 'format', 'img', 'created_at')
    search_fields = ('title', 'format')
    # prepopulated_fields = {'slug': ('name',)}

    def created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')


admin.site.register(Event, EventAdmin)
