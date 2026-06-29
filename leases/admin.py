from django.contrib import admin
from .models import Lease

# Register your models here.
@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'start_date', 'end_date', 'rent_amount', 'payment_frequency', 'active')
    list_filter = ('payment_frequency', 'active')
    search_fields = ('tenant__full_name',)