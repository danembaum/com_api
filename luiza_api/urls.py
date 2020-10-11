from django.urls import path, include
from rest_framework import routers
from .views import DestinatarioViewSets, AgendamentoMensagemViewSets, ModoEnvioViewSets 

router = routers.DefaultRouter()
router.register(r'destinatario', DestinatarioViewSets)
router.register(r'agendamentoMensagem', AgendamentoMensagemViewSets)
router.register(r'modo', ModoEnvioViewSets)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]