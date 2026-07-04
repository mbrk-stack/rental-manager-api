from .views import TenantViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'tenants', TenantViewset, basename='tenant')
urlpatterns = router.urls