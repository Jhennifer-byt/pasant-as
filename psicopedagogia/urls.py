from rest_framework.routers import DefaultRouter
from .views import (
    CicloAcademicoViewSet, EventoViewSet, InstanciaEventoCicloViewSet,
    FotoEventoViewSet, ArchivoInscritosViewSet, CategoriaDeporteViewSet,
    EquipoCopaTecsupViewSet
)

router = DefaultRouter()
router.register('ciclos', CicloAcademicoViewSet)
router.register('eventos', EventoViewSet)
router.register('instancias', InstanciaEventoCicloViewSet)
router.register('fotoevento', FotoEventoViewSet)
router.register('archivos', ArchivoInscritosViewSet)
router.register('categorias', CategoriaDeporteViewSet)
router.register('equipos', EquipoCopaTecsupViewSet)

urlpatterns = router.urls
