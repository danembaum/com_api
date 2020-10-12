""" 
Módulo que contém os modelos para as classes Destinatario, ModoEnvio e Mensagem
para obtenção de dados do Banco de Dados
"""

from django.db import models

# Modelo para destinatário da mensagem
class Destinatario(models.Model):
    """ 
    Classe Destinatario define as informações do destinatário da mensagem
     """
    #definição de campos para a classe Destinatario
    dest_id = models.AutoField(auto_created=True, primary_key=True, null=False, default=None)
    cpf = models.CharField(max_length=14, null=False, unique=True)
    nome = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=30, null=False)
    celular = models.CharField(max_length=14, null=False)

    def __str__(self):
        """
        Função que retorna o campo nome como string representante da instância do objeto Destinatario
        """
        return self.nome


# Modelo para modo de envio da mensagem (E-mail, Whatsapp, SMS e Push)
class ModoEnvio(models.Model):
    """
    Classe ModoEnvio define a plataforma a qual a mensagem será destinada
    """
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        """
        Função que retorna o campo nome como string representante da instância do objeto ModoEnvio
        """
        return self.nome

# Modelo para cadastro de mensagem
class Mensagem(models.Model):
    """
    Classe Mensagem define a mensagem que será agendada para envio, com seus respectivos destinatários 
    e plataforma de envio
    """
    #uma mensagem pode ser enviada para muitos destinatários, assim como um destinatário pode receber várias mensagens
    destinatario = models.ManyToManyField(Destinatario, related_name='destinatarios')
    titulo = models.CharField(max_length=100, null=True)
    texto = models.TextField(null=False)
    data_envio = models.DateField(null=False)
    hora_envio = models.TimeField(null=False)
    status = models.BooleanField(default=False)
    #uma mensagem pode ser enviada por diversos modos de envio, assim como cada um desses modos de envio podem receber diversas mensagens
    modo = models.ForeignKey(ModoEnvio, related_name='envio', null=False, on_delete = models.CASCADE)

    #Função para exibir um texto para status de envio da mensagem ao invés de Boolean
    def enviado(self):
        """
        Função para exibir o status de envio da mensagem como um texto ao invés de boolean
        """
        if self.status:
            return 'Enviada'
        return 'Não enviada'

