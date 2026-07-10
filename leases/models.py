from django.db import models
from tenants.models import Tenant

# Create your models here.
class PaymentFrequency(models.TextChoices):
    MONTHLY = 'MONTHLY', 'Mensuel'
    QUARTERLY = 'QUARTERLY', 'Trimestriel'
    SEMI_ANNUAL = 'SEMI_ANNUAL', 'Semestriel'
    YEARLY = 'YEARLY', 'Annuel'

class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='leases')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=0)
    payment_frequency = models.CharField(max_length=20, choices=PaymentFrequency.choices)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Contrat de {self.tenant.full_name} du {self.start_date} au {self.end_date}"