# Generated by Django 4.0.4 on 2023-05-02 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Partida', '0002_partida_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='resultado',
            field=models.CharField(max_length=8, null=True, verbose_name='Resultado'),
        ),
    ]
