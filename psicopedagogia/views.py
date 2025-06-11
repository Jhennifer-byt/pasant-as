from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (
    CicloAcademico, Evento, MiembroPsicopedagogia, InstanciaEventoCiclo, ImagenGeneralNosotros,
    FotoEvento, ArchivoInscritos, CategoriaDeporte, EquipoCopaTecsup
)
from .serializers import (
    CicloAcademicoSerializer, EventoSerializer, InstanciaEventoCicloSerializer, MiembroPsicopedagogiaSerializer,
    ImagenGeneralNosotrosSerializer, FotoEventoSerializer, ArchivoInscritosSerializer,
    CategoriaDeporteSerializer, EquipoCopaTecsupSerializer
)


class CicloAcademicoViewSet(viewsets.ModelViewSet):
    queryset = CicloAcademico.objects.all()
    serializer_class = CicloAcademicoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'])
    def archivados(self, request):
        archivados = self.queryset.filter(estado='archivado')
        serializer = self.get_serializer(archivados, many=True)
        return Response(serializer.data)


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        ciclo_id = self.request.query_params.get('ciclo')
        if ciclo_id:
            return Evento.objects.filter(ciclo_academico_id=ciclo_id)
        return super().get_queryset()

    @action(detail=False, methods=['get'])
    def destacados(self, request):
        # 🔥 Aquí NO usamos get_queryset para evitar el filtro por ciclo
        eventos_destacados = Evento.objects.filter(es_destacado=True)
        serializer = self.get_serializer(eventos_destacados, many=True)
        return Response(serializer.data)
    
class InstanciaEventoCicloViewSet(viewsets.ModelViewSet):
    queryset = InstanciaEventoCiclo.objects.all()
    serializer_class = InstanciaEventoCicloSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        evento_id = self.request.query_params.get('evento')
        ciclo_id = self.request.query_params.get('ciclo')
        qs = self.queryset

        if evento_id:
            qs = qs.filter(evento_id=evento_id)
        if ciclo_id:
            qs = qs.filter(ciclo_academico_id=ciclo_id)

        return qs


class MiembroPsicopedagogiaViewSet(viewsets.ModelViewSet):
    queryset = MiembroPsicopedagogia.objects.all()
    serializer_class = MiembroPsicopedagogiaSerializer
    permission_classes = [AllowAny]


class ImagenGeneralNosotrosViewSet(viewsets.ModelViewSet):
    queryset = ImagenGeneralNosotros.objects.all()
    serializer_class = ImagenGeneralNosotrosSerializer
    permission_classes = [AllowAny]

class FotoEventoViewSet(viewsets.ModelViewSet):
    queryset = FotoEvento.objects.all()
    serializer_class = FotoEventoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        instancia_id = self.request.query_params.get('instancia')
        if instancia_id:
            return FotoEvento.objects.filter(instancia_id=instancia_id)
        return super().get_queryset()


class ArchivoInscritosViewSet(viewsets.ModelViewSet):
    queryset = ArchivoInscritos.objects.all()
    serializer_class = ArchivoInscritosSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        instancia_id = self.request.query_params.get('instancia')
        if instancia_id:
            return ArchivoInscritos.objects.filter(instancia_id=instancia_id)
        return super().get_queryset()


class CategoriaDeporteViewSet(viewsets.ModelViewSet):
    queryset = CategoriaDeporte.objects.all()
    serializer_class = CategoriaDeporteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EquipoCopaTecsupViewSet(viewsets.ModelViewSet):
    queryset = EquipoCopaTecsup.objects.all()
    serializer_class = EquipoCopaTecsupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        instancia_id = self.request.query_params.get('instancia')
        if instancia_id:
            return EquipoCopaTecsup.objects.filter(instancia_id=instancia_id)
        return super().get_queryset()
