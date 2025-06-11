from rest_framework import serializers
from .models import (
    CicloAcademico, Evento, InstanciaEventoCiclo, MiembroPsicopedagogia, ImagenGeneralNosotros,
    FotoEvento, ArchivoInscritos, CategoriaDeporte, EquipoCopaTecsup
)

class CicloAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CicloAcademico
        fields = '__all__'


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class InstanciaEventoCicloSerializer(serializers.ModelSerializer):
    evento = EventoSerializer(read_only=True)
    ciclo_academico = CicloAcademicoSerializer(read_only=True)

    class Meta:
        model = InstanciaEventoCiclo
        fields = '__all__'

class MiembroPsicopedagogiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiembroPsicopedagogia
        fields = '__all__'


class ImagenGeneralNosotrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenGeneralNosotros
        fields = '__all__'


class FotoEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotoEvento
        fields = '__all__'


class ArchivoInscritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivoInscritos
        fields = '__all__'


class CategoriaDeporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaDeporte
        fields = '__all__'


class EquipoCopaTecsupSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipoCopaTecsup
        fields = '__all__'
