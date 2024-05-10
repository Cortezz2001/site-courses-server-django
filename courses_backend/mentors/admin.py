from django.contrib import admin
from .models import (
    LearnedCourse,
    Mentor,
)
from django.utils.html import format_html

class MentorInline(admin.TabularInline):
    model = Mentor
    extra = 1


class CourseInline(admin.TabularInline):
    model = LearnedCourse
    extra = 1

class MentorAdmin(admin.ModelAdmin):
    inlines = [
        CourseInline,
    ]
    list_display = ('id', 'display_img', 'name', 'role',  'created_at')
    search_fields = ('name', 'role')
    # prepopulated_fields = {'slug': ('name',)}
    def display_img(self, obj):
        return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format(obj.img))

    display_img.short_description = 'Фото'
    
    
    def created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')


admin.site.register(Mentor, MentorAdmin)
