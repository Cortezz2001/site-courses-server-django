# Generated by Django 5.0.6 on 2024-05-16 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_timeline'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='text_kk',
            field=models.TextField(null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='course',
            name='control_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Форма контроля'),
        ),
        migrations.AddField(
            model_name='course',
            name='control_kk',
            field=models.CharField(max_length=255, null=True, verbose_name='Форма контроля'),
        ),
        migrations.AddField(
            model_name='course',
            name='control_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Форма контроля'),
        ),
        migrations.AddField(
            model_name='course',
            name='desc_en',
            field=models.TextField(null=True, verbose_name='Описание курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='desc_kk',
            field=models.TextField(null=True, verbose_name='Описание курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='desc_ru',
            field=models.TextField(null=True, verbose_name='Описание курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='format_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Формат'),
        ),
        migrations.AddField(
            model_name='course',
            name='format_kk',
            field=models.CharField(max_length=255, null=True, verbose_name='Формат'),
        ),
        migrations.AddField(
            model_name='course',
            name='format_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Формат'),
        ),
        migrations.AddField(
            model_name='course',
            name='goal_en',
            field=models.TextField(null=True, verbose_name='Цель курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='goal_kk',
            field=models.TextField(null=True, verbose_name='Цель курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='goal_ru',
            field=models.TextField(null=True, verbose_name='Цель курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='result_en',
            field=models.TextField(null=True, verbose_name='Результаты курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='result_kk',
            field=models.TextField(null=True, verbose_name='Результаты курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='result_ru',
            field=models.TextField(null=True, verbose_name='Результаты курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Название курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='title_kk',
            field=models.CharField(max_length=255, null=True, verbose_name='Название курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название курса'),
        ),
        migrations.AddField(
            model_name='features',
            name='item_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='features',
            name='item_kk',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='features',
            name='item_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='features',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='features',
            name='title_kk',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='features',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='knowhow',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Студент должен знать'),
        ),
        migrations.AddField(
            model_name='knowhow',
            name='text_kk',
            field=models.TextField(null=True, verbose_name='Студент должен знать'),
        ),
        migrations.AddField(
            model_name='knowhow',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Студент должен знать'),
        ),
        migrations.AddField(
            model_name='program',
            name='marker_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Маркер'),
        ),
        migrations.AddField(
            model_name='program',
            name='marker_kk',
            field=models.CharField(max_length=255, null=True, verbose_name='Маркер'),
        ),
        migrations.AddField(
            model_name='program',
            name='marker_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Маркер'),
        ),
        migrations.AddField(
            model_name='program',
            name='theme_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='program',
            name='theme_kk',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='program',
            name='theme_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='skill',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Студент должен уметь'),
        ),
        migrations.AddField(
            model_name='skill',
            name='text_kk',
            field=models.TextField(null=True, verbose_name='Студент должен уметь'),
        ),
        migrations.AddField(
            model_name='skill',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Студент должен уметь'),
        ),
    ]