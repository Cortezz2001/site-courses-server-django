# Generated by Django 5.0.4 on 2024-05-08 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_created_at_alter_event_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания события'),
        ),
    ]
