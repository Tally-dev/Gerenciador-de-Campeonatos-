# Generated by Django 4.0.4 on 2023-04-19 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, null=True, verbose_name='Nome')),
                ('qtdequipe', models.IntegerField(max_length=2, null=True, verbose_name='Quantidade de equipes')),
                ('tipopartida', models.CharField(max_length=200, null=True, verbose_name='Campeonatos')),
            ],
        ),
    ]