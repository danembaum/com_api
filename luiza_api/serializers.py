""" 
Módulo que contém os serializers para os modelos Destinatario, ModoEnvio e Mensagem
definidos em models.py

Os serializers definidos aqui serão utilizados nas ModelViewSets definidas em views.py
"""

from rest_framework import serializers
from .models import Destinatario, Mensagem, ModoEnvio
import datetime

class DestinatarioSerializer(serializers.ModelSerializer):
    """ Classe DestinatarioSerializer """
    class Meta:
        """
        Definindo Destinatario como modelo no qual o serializer deve obter os dados para serializar,
        assim como os campos que devem constar no formato JSON
        """
        model = Destinatario
        fields = ('dest_id','cpf', 'nome', 'email', 'celular')

    def validate_cpf(self, cpf):
        """ 
        Função para validar e formatar o CPF 
        """
        #verificando se CPF contem letras
        if not cpf.isnumeric():
            raise serializers.ValidationError("CPF deve conter apenas números!")
        #verificando se CPF tem tamanho menor que 11
        elif len(cpf) < 11 or len(cpf) > 11:
            raise serializers.ValidationError("CPF deve ter 11 digitos!(Foram digitados {} números)".format(str(len(cpf))))
        else:
            #aplicando máscara de formato do CPF
            cpf = self.createCPFMask(cpf)
        return cpf

    
    def validate_nome(self, nome):
        """
        Função para validar o nome do destinatário 
        """
        if nome.isalnum():
            raise serializers.ValidationError("Nome não deve conter números!")
        return nome

    
    def validate_celular(self, celular):
        """ 
        Função para validar e formatar o campo Celular  
        """    
        #verificando se celular contem letras
        if not celular.isnumeric():
            raise serializers.ValidationError("Número de celular deve conter apenas números!")
        #verificando se numero de celular tem 11 digitos
        elif len(celular) < 11 or len(celular) > 11:
            raise serializers.ValidationError("Número de celular deve ter 11 digitos! (Foram digitados {} números)".format(str(len(celular))))
        else:
            celular = self.createCelMask(celular)
        return celular


    def createCelMask(self, value):
        """ 
        Função para criar o formato de número de celular: (##)#####-#### 
        """
        celular = '(' + value[:2] + ')' + value[2:7] + '-' + value[7:]
        return celular


    def createCPFMask(self, value):
        """ 
        Função para criar o formato de número de CPF: ###.###.###-## 
        """
        cpf = value[:3] + '.' + value[3:6] + '.' + value[6:9] + '-' + value[9:]
        return cpffrom rest_framework import serializers
from .models import Destinatario, Mensagem, ModoEnvio
import datetime

class DestinatarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinatario
        fields = ('dest_id','cpf', 'nome', 'email', 'celular')

    #função para validar CPF
    def validate_cpf(self, cpf):
        #verificando se CPF contem letras
        if not cpf.isnumeric():
            raise serializers.ValidationError("CPF deve conter apenas números!")
        #verificando se CPF tem tamanho menor que 11
        elif len(cpf) < 11 or len(cpf) > 11:
            raise serializers.ValidationError("CPF deve ter 11 digitos!(Foram digitados {} números)".format(str(len(cpf))))
        else:
            #aplicando máscara de formato do CPF
            cpf = self.createCPFMask(cpf)
        return cpf

    #função para validar nome 
    def validate_nome(self, nome):
        if nome.isalnum():
            raise serializers.ValidationError("Nome não deve conter números!")
        return nome

    #função para validar número de celular
    def validate_celular(self, celular):
        
        #verificando se celular contem letras
        if not celular.isnumeric():
            raise serializers.ValidationError("Número de celular deve conter apenas números!")
        #verificando se numero de celular tem 11 digitos
        elif len(celular) < 11 or len(celular) > 11:
            raise serializers.ValidationError("Número de celular deve ter 11 digitos! (Foram digitados {} números)".format(str(len(celular))))
        else:
            celular = self.createCelMask(celular)
        return celular

    #função para criar máscara para telefone celular (##)#####-####
    def createCelMask(self, value):
        celular = '(' + value[:2] + ')' + value[2:7] + '-' + value[7:]
        return celular

    #função para criar máscara de CPF (###.###.###-##)
    def createCPFMask(self, value):
        cpf = value[:3] + '.' + value[3:6] + '.' + value[6:9] + '-' + value[9:]
        return cpf

#Serializer para Plataformas de envio
class ModoEnvioSerializer(serializers.ModelSerializer):
    """ Classe ModoEnvioSerializer """
    class Meta:
        """
        Definindo ModoEnvio como modelo no qual o serializer deve obter os dados para serializar,
        assim como os campos que devem constar no formato JSON
        """
        model = ModoEnvio
        fields = ('id','nome')

#Serializer para envio de mensagem
class MensagemSerializer(serializers.ModelSerializer):
    """ Classe MensagemSerializer """
    #obtendo o resultado da função "enviado" do modelo Mensagem
    enviado = serializers.ReadOnlyField()
    #obtendo todos os destinatários cadastrados 
    destinatario = serializers.PrimaryKeyRelatedField(
        queryset = Destinatario.objects.all().order_by('dest_id'), many=True
    )
    
    #obtendo as plataformas de envio
    modo = ModoEnvioSerializer 

        class Meta:
        """
        Definindo Mensagem como modelo no qual o serializer deve obter os dados para serializar,
        assim como os campos que devem constar no formato JSON
        """
        model = Mensagem
        fields = ('id','titulo', 'texto', 'data_envio', 'hora_envio','modo','enviado','destinatario')
    
    def validate_destinatario(self, dest):
        """
        Função para validar campo destinatário
        """
        #verificando se ao menos um destinatário foi escolhido
        if len(dest) == 0:
            raise serializers.ValidationError("Deve ser escolhido ao menos um destinatário para o envio da mensagem.")
        return dest

    #validação para o texto
    def validate_texto(self, texto):
        """ 
        Função para validar campo texto 
        """
        if len(texto) < 5:
            raise serializers.ValidationError("O texto da mensagem é muito pequeno.")
        return texto

    def validate_data_envio(self, data):
        """ 
        Função para validar campo data_envio 
        """
        #validando a data para envio da mensagem
        if data < datetime.date.today():
            raise serializers.ValidationError("Data inválida! Cadastrastre datas a partir da data atual.")
        return data
            
    def validate(self, validated_data):
        """ 
        Função para validação genérica de campos do modelo Mensagem 
        """
        titulo = validated_data['titulo'] 
        texto = validated_data['texto']
        hora = validated_data['hora_envio']
        modo = validated_data['modo']
        dest = validated_data['destinatario']
        data = validated_data['data_envio']

        #verificando se mensagens de E-mail ou Push possuem título
        if (modo.nome == 'E-mail' or modo.nome == 'Push') and titulo is None:
            raise serializers.ValidationError("Mensagens de {} devem ter um título.".format(modo.nome))
 
        #verificando se o texto das mensagens Push possuem o número de caracteres adequado
        if modo.nome == 'Push' and len(texto) > 50:
            raise serializers.ValidationError("Mensagens de Push devem ter até 50 caracteres. (Foram digitados {} caracteres)".format(str(len(texto))))
        
        #verificando se o texto das mensagens SMS possuem o número de caracteres adequado
        if modo.nome == 'SMS' and len(texto) > 160:
            raise serializers.ValidationError("Mensagens de SMS devem ter até 160 caracteres. (Foram digitados {} caracteres)".format(str(len(texto))))
        
        #validando hora de envio da mensagem
        if data == datetime.date.today() and hora < datetime.datetime.now().time():
            raise serializers.ValidationError("Horário inválido! Cadastrastre horários a partir de horário atual.")
        else:
            pass

        return validated_data