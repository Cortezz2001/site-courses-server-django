from django.db import models


class Mentor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="ФИО")
    exp = models.IntegerField(verbose_name="Стаж")
    img = models.URLField(verbose_name="Фото")
    desc = models.TextField(verbose_name="Награды")
    role = models.CharField(max_length=255, verbose_name="Должность")
    education = models.TextField(verbose_name="Образование")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    class Meta:
        verbose_name = "Тренер"  
        verbose_name_plural = "Тренеры"

    def __str__(self):
        return self.name
class LearnedCourse(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Название")
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Преподаваемая дисциплина"  
        verbose_name_plural = "Преподаваемые дисциплины"

    def __str__(self):
        return self.title