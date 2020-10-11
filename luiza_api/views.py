#from django.shortcuts import render
from rest_framework import viewsets

from .serializers import DestinatarioSerializer, MensagemSerializer, ModoEnvioSerializer
from .models import Destinatario, Mensagem, ModoEnvio

#ModelViewSet para Manipular dados de Destinatarios
class DestinatarioViewSets(viewsets.ModelViewSet):
    queryset =  Destinatario.objects.all().order_by('dest_id')
    serializer_class = DestinatarioSerializer

#ModelViewSet para agendamento de mensagem
class AgendamentoMensagemViewSets(viewsets.ModelViewSet):
    queryset =  Mensagem.objects.all().order_by('data_envio')
    serializer_class = MensagemSerializer

class ModoEnvioViewSets(viewsets.ModelViewSet):
    queryset = ModoEnvio.objects.all()
    serializer_class = ModoEnvioSerializer
# Create your views here.
