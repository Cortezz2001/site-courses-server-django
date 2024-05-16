from modeltranslation.translator import translator, TranslationOptions
from .models import Mentor, LearnedCourse

class MentorTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'role', 'education',)

class LearnedCourseTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Mentor, MentorTranslationOptions)
translator.register(LearnedCourse, LearnedCourseTranslationOptions)