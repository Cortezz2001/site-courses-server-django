from django.db import models

class Mentor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="ФИО", default='ФИО')
    exp = models.CharField(max_length=255, verbose_name="Стаж", default='Стаж')
    img = models.URLField(verbose_name="Фото")
    desc = models.TextField(verbose_name="Описание", default='Описание')
    role = models.CharField(max_length=255, verbose_name="Должность", default='Роль')
    education = models.TextField(verbose_name="Образование", default='Образование')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    class Meta:
        verbose_name = "Тренер"  
        verbose_name_plural = "Тренеры"


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Заголовок", default='Зоголовок')
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Курс"  
        verbose_name_plural = "Курсы"