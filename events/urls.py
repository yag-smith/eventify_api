from rest_framework.routers import DefaultRouter
from .views import EventoViewSet, OrganizadorViewSet

router = DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'organizadores', OrganizadorViewSet)

urlpatterns = router.urls
