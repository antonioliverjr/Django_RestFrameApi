# Generated by Django 4.0.2 on 2022-02-18 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ponto_turisticos', '0003_pontoturistico_eventos'),
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='ponto_tur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ponto_turisticos.pontoturistico'),
        ),
    ]
