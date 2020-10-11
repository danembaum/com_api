from django.db import models

# Modelo para destinatário da mensagem
class Destinatario(models.Model):
    dest_id = models.AutoField(auto_created=True, primary_key=True, null=False, default=None)
    cpf = models.CharField(max_length=14, null=False, unique=True)
    nome = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=30, null=False)
    celular = models.CharField(max_length=14, null=False)

    def __str__(self):
        return self.nome

# Modelo para modo de envio da mensagem (E-mail, Whatsapp, SMS e Push)
class ModoEnvio(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

# Modelo para cadastro de mensagem
class Mensagem(models.Model):
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
        if self.status:
            return 'Enviada'
        return 'Não enviada'

