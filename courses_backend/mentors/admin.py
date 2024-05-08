from django.contrib import admin
from .models import (
    LearnedCourse,
    Mentor,
)

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
    list_display = ('id', 'name', 'role', 'img', 'created_at')
    search_fields = ('name', 'role')
    # prepopulated_fields = {'slug': ('name',)}

    def created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')


admin.site.register(Mentor, MentorAdmin)
