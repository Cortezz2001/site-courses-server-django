# Generated by Django 5.0.4 on 2024-05-08 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0002_remove_mentor_active_courses_mentor_active_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='active_courses',
        ),
    ]