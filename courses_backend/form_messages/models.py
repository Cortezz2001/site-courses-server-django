from django.db import models

class FormMessage(models.Model):
    name = models.CharField(max_length=100, blank=True, verbose_name="Имя")
    number = models.CharField(max_length=12, blank=True, verbose_name="Номер телефона") 
    email = models.EmailField(verbose_name="Почта")
    messenger = models.CharField(max_length=50, blank=True, verbose_name="Мессенджер")
    messenger_username = models.CharField(max_length=100, blank=True, verbose_name="username мессенджера")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение"  
        verbose_name_plural = "Сообщения"
        
    def __str__(self):
        return self.email