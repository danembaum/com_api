"""
Suite de testes para views.py
Como o objetivo do desafio era criar endpoints para agendamento de mensagem, foram implementados
apenas testes para AgendamentoMensagemViewSet. No futuro, como forma de aprendizado pessoal, serão
implementados para as outras ViewSets definidas em views.py
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

from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


class TestAgendamentoMensagem:
    """
    Classe para testar a AgendamendoMensagemView
    """
    def setup(self):
        """
        Definição de setup para testes
        """
        self.client = APIClient()
        self.url = reverse('mensagem-list')

        #criando instância de Destinatario com id=3
        self.dest = mixer.blend(Destinatario, id=3, email="teste@django.com")
        #criando instância de ModoEnvio id=1
        self.modoEnvio = mixer.blend(ModoEnvio, id=1)
        #setando data atual
        self.data = datetime.date.today()
        #setando hora para daqui 30 minutos
        self.hora = datetime.datetime.now() + datetime.timedelta(minutes=30)

    def test_list_agendamento(self):
        """
        Teste de listagem de objetos
        """

        #criando mensagem com valores aleatórios, com Destinatario especificado
        agendamento = mixer.blend(Mensagem, destinatario=self.dest, modo = self.modoEnvio)

        response = self.client.get(self.url)
      
        assert response.json() is not None
        assert len(response.json()) == 1
        assert response.status_code == 200

    def getDictionary(self, data):
        """
        Função para converter modelo Mensagem em dictionary

        Args:
            data (Mensagem): instância a ser convertida em dictionary

        Returns:
            Dictionary: Dictionary contendo os campos de Mensagem
        """
        #serializando o objeto mensagem
        serializer = MensagemSerializer(instance=data)
        #criando um json do objeto serializado (byte)
        jsontest = JSONRenderer().render(serializer.data)
        #criando um buffer
        stream = io.BytesIO(jsontest)
        #criando dictionary
        post_data = JSONParser().parse(stream)

        return post_data

    def doPost(self, data):
        """
        Função para POST de Mensagem

        Args:
            data (Mensagem): Instância de Mensagem

        Returns:
            rest_framework.response.Response: Resposta de POST (status_code, json)
        """
        post_data = self.getDictionary(data)

        return self.client.post(self.url, data = post_data)

    def test_create_agendamento(self):
        """
        Teste de criação de agendamento
        """
        #criando mensagem com valores aleatórios, com Destinatario especificado
        agendamento = mixer.blend(Mensagem, destinatario = self.dest, modo = self.modoEnvio, 
            data_envio = self.data, hora_envio = self.hora.time())

        response = self.doPost(agendamento)
    
        assert response.json() is not None
        assert response.status_code == 201

    def test_create_invalid_agendamento_data(self):
        """
        Teste de criação de agendamento com data inválida
        """
        #criando segunda mensagem com valores aleatórios, com Destinatario especificado, com data inválida
        agendamento = mixer.blend(Mensagem, destinatario = self.dest, modo = self.modoEnvio, 
            data_envio = '2020-01-01', hora_envio = self.hora.time())

        response = self.doPost(agendamento)
        assert response.status_code == 400

    def test_create_invalid_agendamento_hora(self):
        """
        Teste de criação de agendamento com hora inválida
        """
        #criando terceira mensagem com valores aleatórios, com Destinatario especificado, com hora inválida
        agendamento = mixer.blend(Mensagem, destinatario = self.dest, modo = self.modoEnvio, 
            data_envio = self.data, hora_envio = datetime.datetime.now().time())

        response = self.doPost(agendamento)
        assert response.status_code == 400

    def test_create_invalid_agendamento_titulo(self):
        """
        Teste de criação de agendamento com titulo inválido para E-mail ou Push
        """
        #criando mensagem com valores aleatórios, com Destinatario especificado, com título (Modo: E-mail)
        agendamento = mixer.blend(Mensagem, titulo = "", destinatario = self.dest, modo = self.modoEnvio, 
            data_envio = self.data, hora_envio = datetime.datetime.now().time())

        response = self.doPost(agendamento)
        assert response.status_code == 400

        modo = mixer.blend(ModoEnvio, id=4)
         #criando segunda mensagem com valores aleatórios, com Destinatario especificado, com título (Modo: Push)
        agendamento2 = mixer.blend(Mensagem, titulo = "", destinatario = self.dest, modo = modo, 
            data_envio = self.data, hora_envio = datetime.datetime.now().time())

        response = self.doPost(agendamento2)
        assert response.status_code == 400

    def test_delete_agendamento(self):
        """
        Função para teste de exclusão de agendamento
        """
        mensagem = mixer.blend(Mensagem, pk = 1)
        assert Mensagem.objects.count() == 1

        url = reverse("mensagem-detail", kwargs={"pk": 1})
        print("URL: ", url)
        response = self.client.delete(url)

        assert response.status_code == 204

        assert Mensagem.objects.count() == 0