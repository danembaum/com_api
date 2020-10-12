"""
Suite de testes para serializers.py
Como o objetivo do desafio era criar endpoints para agendamento de mensagem, foram implementados
apenas testes para MensagemSerializer. No futuro, como forma de aprendizado pessoal, serão
implementados para as outras ViewSets definidas em serializers.py
"""

from django.urls import reverse
import pytest
from .models import Destinatario, Mensagem, ModoEnvio
from .serializers import MensagemSerializer
from mixer.backend.django import mixer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
import io
import datetime

pytestmark = pytest.mark.django_db

class TesteMensagemSerializer:
    """
    Classe para teste de MensagemSerializer
    """

    def setup(self):
        """
        Definição de setup para testes
        """
        #criando instância de Destinatario com id=3
        self.dest = mixer.blend(Destinatario, id=3, email="teste@django.com")
        #criando instância de ModoEnvio id=1
        self.modoEnvio = mixer.blend(ModoEnvio, id=1)
        #setando data atual
        self.data = datetime.date.today()
        #setando hora para daqui 30 minutos
        self.hora = datetime.datetime.now() + datetime.timedelta(minutes=30)
        self.agendamento = mixer.blend(Mensagem, destinatario= self.dest, modo = self.modoEnvio, data_envio = self.data, 
                hora_envio = self.hora)

    def test_mensagem_count_fields(self):
        """
        Função para verificar se a quantidade de campos está de acordo com a definida em MensagemSerializer (serializers.py)
        """
        serializer = MensagemSerializer(self.agendamento)

        assert len(serializer.data.keys()) == 8 

    def test_mensagem_fields(self):
        """
        Função para verificar se os campos estão de acordo com o definido em MensagemSerializer (serializers.py)
        """
        serializer = MensagemSerializer(self.agendamento)

        assert set(serializer.data.keys()) == set(['id','titulo', 'texto', 'data_envio', 'hora_envio','modo','enviado','destinatario'])
    
    def test_mensagem_hora_invalida(self):
        """
        Função para verificar se mensagem com horário incorreto é inválida
        """
        agendamento = mixer.blend(Mensagem, destinatario= self.dest, modo = self.modoEnvio, data_envio = self.data, 
                hora_envio = datetime.datetime.now().time())
        
        serializer = MensagemSerializer(data=agendamento)
        assert not serializer.is_valid()


    def test_mensagem_data_invalida(self):
        """
        Função para verificar se mensagem com horário incorreto é inválida
        """
        agendamento = mixer.blend(Mensagem, destinatario= self.dest, modo = self.modoEnvio, data_envio = '2020-01-01', 
                hora_envio = self.hora)
        
        serializer = MensagemSerializer(data=agendamento)
        assert not serializer.is_valid()
        assert serializer.error_messages == "Horário inválido! Cadastrastre horários a partir de horário atual."

    def test_mensagem_data_invalida(self):
        """
        Função para verificar se mensagem com data incorreta é inválida
        """
        agendamento = mixer.blend(Mensagem, destinatario= self.dest, modo = self.modoEnvio, data_envio = '2020-01-01', 
                hora_envio = self.hora)
        
        serializer = MensagemSerializer(data=agendamento)
        assert not serializer.is_valid()

    def test_mensagem_titulo_email(self):
        """
        Função para verificar se mensagem de E-mail ou Push sem título é inválida
        """
        #criando mensagem com valores aleatórios, com Destinatario especificado, com título (Modo: E-mail)
        agendamento = mixer.blend(Mensagem, titulo = "", destinatario = self.dest, modo = self.modoEnvio, 
            data_envio = self.data, hora_envio = datetime.datetime.now().time())

        
        serializer = MensagemSerializer(data=agendamento)
        assert not serializer.is_valid()

        modo = mixer.blend(ModoEnvio, id=4)
         #criando segunda mensagem com valores aleatórios, com Destinatario especificado, com título (Modo: Push)
        agendamento2 = mixer.blend(Mensagem, titulo = "", destinatario = self.dest, modo = modo, 
            data_envio = self.data, hora_envio = datetime.datetime.now().time())

        serializer = MensagemSerializer(data=agendamento2)
        assert not serializer.is_valid()
