from django.db import models
from mentors.models import Mentor


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Название курса")
    bid = models.CharField(max_length=255, blank=True, verbose_name="Наименование программы, куда входит курс")
    img = models.URLField(verbose_name="Изображение")
    desc = models.TextField(verbose_name="Описание курса")
    goal = models.TextField(verbose_name="Цель курса")
    active_mentors = models.ManyToManyField(Mentor, blank=True, verbose_name="Тренеры курса")
    price = models.CharField(max_length=255, verbose_name="Цена курса")
    format = models.CharField(max_length=255, verbose_name="Формат")
    result = models.TextField(verbose_name="Результаты курса")
    control = models.CharField(max_length=255, verbose_name="Форма контроля")
    timeline = models.IntegerField(verbose_name="Длительность курса (Недели)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания курса')
    class Meta:
        verbose_name = "Курс"  
        verbose_name_plural = "Курсы"    
    def __str__(self):
        return self.title

class Skill(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    text = models.TextField(verbose_name="Студент должен уметь")
    class Meta:
        verbose_name = "Навык"  
        verbose_name_plural = "Навыки"    

class Knowhow(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    text = models.TextField(verbose_name="Студент должен знать")
    class Meta:
        verbose_name = "Необходимый навык"  
        verbose_name_plural = "Необходимые навыки"

class Program(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    theme = models.CharField(max_length=255, verbose_name="Название")
    marker = models.CharField(max_length=255, verbose_name="Маркер")
    class Meta:
        verbose_name = "Программа курса"  
        verbose_name_plural = "Программа курса"

class Features(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=255, verbose_name="Название")
    title = models.CharField(max_length=255, verbose_name="Описание")
    class Meta:
        verbose_name = "Дополнительная информация (Пример: Форма обучения - Оффлайн)"  
        verbose_name_plural = "Дополнительная информация (Пример: Форма обучения - Оффлайн)"





class Challenge(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    text = models.TextField(verbose_name="Название")
    class Meta:
        verbose_name = "Задача"  
        verbose_name_plural = "Задачи"
