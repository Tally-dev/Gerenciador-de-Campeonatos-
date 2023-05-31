# Generated by Django 4.0.4 on 2023-05-02 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Campeonato', '0002_alter_campeonato_qtdequipe_and_more'),
        ('Equipe', '0003_equipe_campeonatos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('horario', models.TimeField(verbose_name='Horario')),
                ('local', models.CharField(max_length=30, verbose_name='Local')),
                ('resultado', models.CharField(max_length=8, verbose_name='Resultado')),
                ('placar', models.IntegerField(verbose_name='Placar')),
                ('Campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Campeonato.campeonato')),
                ('Equipe1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PrimeiraEquipe', to='Equipe.equipe')),
                ('Equipe2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SegundaEquipe', to='Equipe.equipe')),
            ],
        ),
    ]