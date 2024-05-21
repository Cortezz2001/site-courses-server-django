from django.db import models

class Banner(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.URLField(verbose_name="Изображение (1330x600)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания баннера')
    class Meta:
        verbose_name = "Баннер"  
        verbose_name_plural = "Баннеры"    

    def __str__(self):
        return "Баннер"