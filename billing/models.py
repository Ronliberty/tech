from django.db import models
from django.contrib.auth.models import User

# Choices for Payment Methods
class PaymentMethod(models.TextChoices):
    BANK = 'Bank', 'Bank'
    CRYPTO = 'Crypto', 'Crypto'
    MPESA = 'MPESA', 'MPESA'


# Invoice Model
class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invoices')
    description = models.TextField()
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    payment_method = models.CharField(
        max_length=10, choices=PaymentMethod.choices, default=PaymentMethod.BANK
    )
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Invoice #{self.id} for {self.user.username}"

    class Meta:
        ordering = ['-due_date']  # Orders invoices by due date, newest first


# Receipt Model
class Receipt(models.Model):
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE, related_name='receipt')
    payment_date = models.DateField()
    payment_reference = models.CharField(max_length=100)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Receipt for Invoice #{self.invoice.id}"

    class Meta:
        ordering = ['-payment_date']  # Orders receipts by payment date, newest first