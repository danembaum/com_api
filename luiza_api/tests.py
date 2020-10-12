"""
Suite de teste para modelos definidos em models.py
"""

from django.urls import reverse
import pytest
from hypothesis import strategies as st, given
from .models import Destinatario, Mensagem, ModoEnvio
from .serializers import MensagemSerializer
from mixer.backend.django import mixer

from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


class TestDestinatarioModel:
    """
    Classe para teste do modelo Destinatario
    """
    
    def test_destinatario_create(self):
        """
        Teste de criação de uma instância de Destinatario
        """
        nome = "Francisco Souza"
        email = "chico@django.com"
        #criando instância de destinatário com valores definidos para nome e email, com os outros
        #campos definidos automáticamente
        destinatario = mixer.blend(Destinatario, nome=nome, email=email)

        destinatario_result = Destinatario.objects.last()

        assert destinatario_result.nome == nome

    def test_str_return(self):
        """
        Teste de retorno __str__ para uma instância de Destinatario
        """
        nome = "Marlene da Silva"
        email = "marlene@django.com"
        destinatario = mixer.blend(Destinatario, nome=nome, email=email)

        destinatario_result = Destinatario.objects.last()

        assert str(destinatario_result) == nome
    

class TestModoEnvioModel:
    """
    Classe para teste do modelo Modo Envio
    """
    def test_modoenvio_create(self):
        """
        Função para testar a criação de uma instância de ModoEnvio
        """
        nome="E-mail"

        modoenvio = mixer.blend(ModoEnvio, nome=nome)

        modo_result = ModoEnvio.objects.last()

        assert modo_result.nome == nome
    
    def test_str_return(self):
        """
        Função para teste do retorno __str__ de uma instância de ModoEnvio
        """
        nome = "Push"

        modoenvio = mixer.blend(ModoEnvio, nome=nome)

        modo_result = ModoEnvio.objects.last()

        assert str(modo_result) == nome


class TestMensagemModel:
    """
    Função para teste do modelo Mensagem
    """

    def test_mensagem_create(self):
        """
        Teste de criação de uma instância de Mensagem
        """
        
        mensagem = mixer.blend(Mensagem)

        mensagem_result = Mensagem.objects.last()

        assert mensagem_result is not None


    def teste_mensagem_destinatario(self):
        """
        Teste para verificar se uma instância de Destinario foi criada para a instância de Mensagem
        """
        mensagem = mixer.blend(Mensagem)

        mensagem_result = Mensagem.objects.last()

        destinatario = mensagem_result.destinatario

        print("DEST: ", destinatario)
        assert destinatario is not None
    
    #dado valores booleanos aleatórios
    @given(st.booleans())
    def test_enviado(self, envio):
        """
        Função para teste do retorno da função enviado    
        Args:
            envio (Boolean): Valores True ou False
        """
        mensagem = mixer.blend(Mensagem, status=envio)

        mensagem_result = Mensagem.objects.last()

        if mensagem_result.status:
            assert mensagem_result.enviado() == 'Enviada'
        else:
            assert mensagem_result.enviado() == 'Não enviada'