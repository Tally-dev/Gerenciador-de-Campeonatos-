# Generated by Django 4.0.4 on 2023-07-17 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Equipe', '0005_equipe_escudo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='escudo',
            field=models.ImageField(null=True, upload_to='escudos/'),
        ),
    ]