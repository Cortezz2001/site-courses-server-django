from django.db import models

class Mentor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    exp = models.CharField(max_length=255)
    img = models.URLField()
    desc = models.TextField()
    role = models.CharField(max_length=255)
    education = models.TextField()


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)