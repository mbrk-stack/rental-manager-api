from django.db import models
from leases.models import Lease

# Create your models here.
class Payment(models.Model):
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE, related_name='payments')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=0)
    payment_date = models.DateField()
    periode_start = models.DateField()
    periode_end = models.DateField()
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Paiement du {self.amount_paid} pour {self.lease} le {self.payment_date}"