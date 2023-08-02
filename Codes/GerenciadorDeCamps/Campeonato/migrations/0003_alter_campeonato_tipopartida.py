# Generated by Django 4.0.4 on 2023-07-17 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campeonato', '0002_alter_campeonato_qtdequipe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campeonato',
            name='tipopartida',
            field=models.CharField(choices=[('1', 'Ponto Corrido'), ('2', 'Mata-Mata'), ('3', 'Fase de Grupo/Mata-Mata'), ('4', 'Cardiologista'), ('5', 'Laringologista')], max_length=1, null=True, verbose_name='Tipo de partida'),
        ),
    ]