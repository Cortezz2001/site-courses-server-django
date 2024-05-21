from modeltranslation.translator import translator, TranslationOptions
from .models import Challenge, Course, Features, Knowhow, Program, Skill

class CourseTranslationOptions(TranslationOptions):
    fields = ('title', 'desc', 'goal', 'format', 'result', 'control')

class SkillTranslationOptions(TranslationOptions):
    fields = ('text',)

class KnowhowTranslationOptions(TranslationOptions):
    fields = ('text',)

class ProgramTranslationOptions(TranslationOptions):
    fields = ('theme', 'marker',)

class FeaturesTranslationOptions(TranslationOptions):
    fields = ('item', 'title',)

class ChallengeTranslationOptions(TranslationOptions):
    fields = ('text',)

translator.register(Course, CourseTranslationOptions)
translator.register(Skill, SkillTranslationOptions)
translator.register(Knowhow, KnowhowTranslationOptions)
translator.register(Program, ProgramTranslationOptions)
translator.register(Features, FeaturesTranslationOptions)
translator.register(Challenge, ChallengeTranslationOptions)