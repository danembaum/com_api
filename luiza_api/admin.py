from django.contrib import admin
from .models import Destinatario, Mensagem

# Register your models here.
admin.site.register(Destinatario)
admin.site.register(Mensagem)