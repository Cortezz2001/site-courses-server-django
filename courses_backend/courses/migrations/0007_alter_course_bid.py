# Generated by Django 5.0.6 on 2024-05-23 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_challenge_text_en_challenge_text_kk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='bid',
            field=models.CharField(blank=True, max_length=255, verbose_name='Наименование программы, куда входит курс'),
        ),
    ]