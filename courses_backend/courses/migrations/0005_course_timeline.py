# Generated by Django 5.0.4 on 2024-05-10 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_course_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='timeline',
            field=models.IntegerField(default=26, verbose_name='Длительность курса (Недели)'),
            preserve_default=False,
        ),
    ]
