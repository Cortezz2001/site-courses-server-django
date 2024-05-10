# Generated by Django 5.0.4 on 2024-05-10 09:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_active_mentors'),
        ('mentors', '0004_alter_learnedcourse_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Theme',
            new_name='Program',
        ),
        migrations.AlterModelOptions(
            name='features',
            options={'verbose_name': 'Дополнительная информация (Пример: Форма обучения - Оффлайн)', 'verbose_name_plural': 'Дополнительная информация (Пример: Форма обучения - Оффлайн)'},
        ),
        migrations.AlterModelOptions(
            name='program',
            options={'verbose_name': 'Программа курса', 'verbose_name_plural': 'Программа курса'},
        ),
        migrations.AddField(
            model_name='course',
            name='control',
            field=models.CharField(default=datetime.datetime(2024, 5, 10, 9, 13, 59, 119284, tzinfo=datetime.timezone.utc), max_length=255, verbose_name='Форма контроля'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='active_mentors',
            field=models.ManyToManyField(blank=True, to='mentors.mentor', verbose_name='Тренеры курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='bid',
            field=models.CharField(max_length=255, unique=True, verbose_name='Наименование программы, куда входит курс'),
        ),
        migrations.AlterField(
            model_name='course',
            name='desc',
            field=models.TextField(verbose_name='Описание курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.CharField(max_length=255, verbose_name='Цена курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название курса'),
        ),
        migrations.DeleteModel(
            name='Control',
        ),
    ]