from django.db import models

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Название", default='Название')
    desc = models.TextField(verbose_name="Описание", default='Описание')
    img = models.URLField(verbose_name="Изображение")
    format = models.CharField(max_length=50, verbose_name="Формат", default='Формат')
    startDate = models.DateField(verbose_name="Дата начала")
    startTime = models.TimeField(verbose_name="Время начала")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания события')

    class Meta:
        verbose_name = "Анонс"  
        verbose_name_plural = "Анонсы"


class Mentor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="ФИО", default='ФИО')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='mentors')
    class Meta:
        verbose_name = "Тренер"  
        verbose_name_plural = "Тренеры"
    