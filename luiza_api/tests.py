from django.test import TestCase
import pytest
from hypothesis import strategies as st, given
from .models import Destinatario, Mensagem, ModoEnvio

from mixer.backend.django import mixer

from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db

# Classe para teste do modelo Destinatario
class TestDestinatarioMode:
    #teste de criação de objeto
    def test_destinatario_create(self):
        nome = "Francisco Souza"
        destinatario = mixer.blend(Destinatario, nome=nome)

        destinatario_result = Destinatario.objects.last()

        assert destinatario_result.nome == nome
    #teste do retorno do método __str__
    def test_str_return(self):
        nome = "Marlene da Silva"
        destinatario = mixer.blend(Destinatario, nome=nome)

        destinatario_result = Destinatario.objects.last()

        assert str(destinatario_result) == nome
    
#Classe para teste do Modelo ModoEnvio
class TestModoEnvioModel:
    #teste de criação do objeto
    def test_modoenvio_create(self):
        nome="E-mail"

        modoenvio = mixer.blend(ModoEnvio, nome=nome)

        modo_result = ModoEnvio.objects.last()

        assert modo_result.nome == nome
    #teste de retorno de __str__
    def test_str_return(self):
        nome = "Push"

        modoenvio = mixer.blend(ModoEnvio, nome=nome)

        modo_result = ModoEnvio.objects.last()

        assert str(modo_result) == nome


#Classe para teste do modelo Mensagem
class TestMensagemModel:
    #teste de criação do objeto
    def test_mensagem_create(self):
        
        mensagem = mixer.blend(Mensagem)

        mensagem_result = Mensagem.objects.last()

        assert mensagem_result is not None

    #teste de criação do destinatario para mensagem
    def teste_mensagem_destinatario(self):
        mensagem = mixer.blend(Mensagem)

        mensagem_result = Mensagem.objects.last()

        destinatario = mensagem_result.destinatario

        print("DEST: ", destinatario)
        assert destinatario is not None
    
    #teste de verificação para saída da função enviado
    @given(st.booleans())
    def test_enviado(self, envio):
        mensagem = mixer.blend(Mensagem, status=envio)

        mensagem_result = Mensagem.objects.last()

        if mensagem_result.status:
            assert mensagem_result.enviado() == 'Enviada'
        else:
            assert mensagem_result.enviado() == 'Não enviada'
   