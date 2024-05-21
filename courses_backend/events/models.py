from django.db import models

from mentors.models import Mentor


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Название")
    desc = models.TextField(verbose_name="Описание")
    active_mentors = models.ManyToManyField(Mentor, blank=True, verbose_name="Ответственные тренеры")
    img = models.URLField(verbose_name="Изображение")
    format = models.CharField(max_length=50, verbose_name="Формат мероприятия")
    startDate = models.DateField(verbose_name="Дата начала")
    startTime = models.TimeField(verbose_name="Время начала")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания события')

    class Meta:
        verbose_name = "Анонс"  
        verbose_name_plural = "Анонсы"

    def __str__(self):
        return self.title
    