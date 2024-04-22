from django.db import models


class Course(models.Model):
    course_name: models.CharField(max_length=200)
    course_data: models.TextField("course data for build")
    pub_date: models.DateField("date of publication", auto_created=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.course_name