from rest_framework import serializers
from .models import Evento, Organizador

class OrganizadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizador
        fields = '__all__'


class EventoSerializer(serializers.ModelSerializer):
    organizador = OrganizadorSerializer(read_only=True)
    organizador_id = serializers.PrimaryKeyRelatedField(
        queryset=Organizador.objects.all(), source='organizador', write_only=True
    )

    class Meta:
        model = Evento
        fields = ['id', 'nombre', 'fecha', 'ubicacion', 'organizador', 'organizador_id']
