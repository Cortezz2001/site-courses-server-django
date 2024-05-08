from django.db import models
from mentors.models import Mentor


class Course(models.Model):
    active_mentors = models.ManyToManyField(Mentor, blank=True)
    id = models.AutoField(primary_key=True)
    bid = models.CharField(max_length=255, unique=True, verbose_name="Программа")
    img = models.URLField(verbose_name="Изображение")
    desc = models.TextField(verbose_name="Описание")
    goal = models.TextField(verbose_name="Цель курса")
    price = models.CharField(max_length=255, verbose_name="Цена")
    title = models.CharField(max_length=255, verbose_name="Название")
    format = models.CharField(max_length=255, verbose_name="Формат")
    result = models.TextField(verbose_name="Результаты курса")
    slug = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания курса')
    class Meta:
        verbose_name = "Курс"  
        verbose_name_plural = "Курсы"    


class Skill(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    text = models.TextField(verbose_name="Студент должен уметь")
    class Meta:
        verbose_name = "Навык"  
        verbose_name_plural = "Навыки"    


class Control(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    item = models.CharField(max_length=255, verbose_name="Форма контроля")
    class Meta:
        verbose_name = "Форма контроля"  
        verbose_name_plural = "Формы контроля"


class Theme(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    theme = models.CharField(max_length=255, verbose_name="Название")
    marker = models.CharField(max_length=255, verbose_name="Маркер")


class Features(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=255, verbose_name="Название")
    title = models.CharField(max_length=255, verbose_name="Описание")
    class Meta:
        verbose_name = "Особенность"  
        verbose_name_plural = "Особенности"


class Knowhow(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    text = models.TextField(verbose_name="Студент должен знать")
    class Meta:
        verbose_name = "Необходимый навык"  
        verbose_name_plural = "Необходимые навыки"


class Challenge(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    text = models.TextField(verbose_name="Название")
    class Meta:
        verbose_name = "Задача"  
        verbose_name_plural = "Задачи"
