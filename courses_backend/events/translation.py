from modeltranslation.translator import translator, TranslationOptions
from .models import Event

class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'desc', 'format', )


translator.register(Event, EventTranslationOptions)