from django.contrib import admin
from .models import (
    Course,
    Skill,
    Control,
    Theme,
    Features,
    Knowhow,
    Challenge,
)

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


class ControlInline(admin.TabularInline):
    model = Control
    extra = 1


class ThemeInline(admin.TabularInline):
    model = Theme
    extra = 1


class FeaturesInline(admin.TabularInline):
    model = Features
    extra = 1


class KnowhowInline(admin.TabularInline):
    model = Knowhow
    extra = 1


class ChallengeInline(admin.TabularInline):
    model = Challenge
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [
        SkillInline,
        ControlInline,
        ThemeInline,
        FeaturesInline,
        KnowhowInline,
        ChallengeInline,
    ]
    list_display = ('id', 'title', 'price', 'img', 'format', 'created_at')
    search_fields = ('title', 'desc')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('active_mentors',)


    def created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')


admin.site.register(Course, CourseAdmin)
