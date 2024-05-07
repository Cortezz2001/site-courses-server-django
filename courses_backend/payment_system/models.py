from django.db import models


class PaymentOperation(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
    )
    
    user_email = models.EmailField(max_length=255, verbose_name='Email address of the payer')
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Payment amount')
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Date of payment reception')
    processing_date = models.DateTimeField(null=True, blank=True, verbose_name='Date of payment processing')
    course_purchased = models.ForeignKey('courses.Course', on_delete=models.CASCADE, verbose_name='Purchased course')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING', verbose_name='Payment status')

    def __str__(self):
        return f"Payment operation for {self.user_email} (amount: {self.payment_amount}) - {self.get_status_display()}"
