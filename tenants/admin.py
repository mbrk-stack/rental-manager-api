from django.contrib import admin
from .models import Tenant

# Register your models here


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'residence_number', 'entry_date', 'active', 'created_at', 'updated_at')
    list_filter = ('active',)
    search_fields = ('full_name', 'phone_number', 'residence_number')