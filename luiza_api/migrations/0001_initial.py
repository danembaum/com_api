# Generated by Django 3.1.2 on 2020-10-10 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destinatario',
            fields=[
                ('dest_id', models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('nome', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('celular', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='ModoEnvio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, null=True)),
                ('texto', models.TextField()),
                ('data_envio', models.DateField()),
                ('hora_envio', models.TimeField()),
                ('status', models.BooleanField(default=False)),
                ('destinatario', models.ManyToManyField(related_name='destinatarios', to='luiza_api.Destinatario')),
                ('modo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='envio', to='luiza_api.modoenvio')),
            ],
        ),
    ]
