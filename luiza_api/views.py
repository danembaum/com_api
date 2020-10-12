"""
Módulo contém as views da API para a realização das operações POST, GET e DELETE
"""

from rest_framework import viewsets

from .serializers import DestinatarioSerializer, MensagemSerializer, ModoEnvioSerializer
from .models import Destinatario, Mensagem, ModoEnvio

#ModelViewSet para Manipular dados de Destinatarios
class DestinatarioViewSets(viewsets.ModelViewSet):
    """
    Classe DestinatarioViewSets
    """
    queryset =  Destinatario.objects.all().order_by('dest_id')
    serializer_class = DestinatarioSerializer

#ModelViewSet para agendamento de mensagem
class AgendamentoMensagemViewSets(viewsets.ModelViewSet):
    """
    Classe AgendamentoMensagemViewSets
    """
    queryset =  Mensagem.objects.all().order_by('data_envio')
    serializer_class = MensagemSerializer

class ModoEnvioViewSets(viewsets.ModelViewSet):
    """
    Classe ModoEnvioViewSets
    """
    queryset = ModoEnvio.objects.all()
    serializer_class = ModoEnvioSerializer