from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from .models import Tenant
from .serializers import TenantSerializer

# Create your views here.
class TenantViewset(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer # indicates which serializer to use for this viewset

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter] # this indicates that these are the tools you can use to filter, order, and search the data in this viewset

    filterset_fields = ['full_name', 'active', 'phone_number'] # this indicates which fields you can filter the data by

    ordering_fields = ['full_name', 'created_at'] # this indicates which fields you can order the data by