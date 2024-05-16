from django.contrib import admin
from .models import (
    Course,
    Skill,
    Program,
    Features,
    Knowhow,
    Challenge,
)
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
class SkillInline(TranslationStackedInline):
    model = Skill
    extra = 1


class ProgramInline(TranslationStackedInline):
    model = Program
    extra = 1


class FeaturesInline(TranslationStackedInline):
    model = Features
    extra = 1


class KnowhowInline(TranslationStackedInline):
    model = Knowhow
    extra = 1


class ChallengeInline(TranslationStackedInline):
    model = Challenge
    extra = 1


class CourseAdmin(TranslationAdmin):
    inlines = [
        SkillInline,
        ProgramInline,
        FeaturesInline,
        KnowhowInline,
        ChallengeInline,
    ]
    list_display = ('id', 'title', 'price', 'format', 'created_at')
    search_fields = ('title', 'desc')
    filter_horizontal = ('active_mentors',)


    def created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')


admin.site.register(Course, CourseAdmin)
