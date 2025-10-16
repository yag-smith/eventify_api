from rest_framework import viewsets, filters
from .models import Evento, Organizador
from .serializers import EventoSerializer, OrganizadorSerializer

class OrganizadorViewSet(viewsets.ModelViewSet):
    queryset = Organizador.objects.all()
    serializer_class = OrganizadorSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'ubicacion']  # Permite búsqueda con ?search=
