from django.contrib import admin
from.models import Payment

# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('lease', 'amount_paid', 'payment_date', 'periode_start', 'periode_end')
    list_filter = ('payment_date',)
    search_fields = ('lease__tenant__full_name',)