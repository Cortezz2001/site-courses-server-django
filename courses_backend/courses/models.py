from django.db import models


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    bid = models.CharField(max_length=255, unique=True)
    img = models.URLField()
    desc = models.TextField()
    goal = models.TextField()
    price = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    format = models.CharField(max_length=255)
    result = models.TextField()
    slug = models.CharField(max_length=255)


class Skill(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    text = models.TextField()


class Control(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    item = models.CharField(max_length=255)


class Mentor(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    exp = models.CharField(max_length=255)
    img = models.URLField()


class Theme(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    theme = models.CharField(max_length=255)
    marker = models.CharField(max_length=255)


class Features(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    learningType = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    countOfWeek = models.IntegerField()
    age = models.CharField(max_length=255)
    countOfLessonPerWeek = models.IntegerField()
    countOfLessonPerYear = models.IntegerField()
    countOfLessonPerYear = models.IntegerField()
    qualification = models.CharField(max_length=255)


class Knowhow(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    text = models.TextField()


class Challenge(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    text = models.TextField()

