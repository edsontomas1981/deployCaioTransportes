# Generated by Django 5.0.6 on 2024-06-18 00:24

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacional', '0056_ocorrencianotasfiscais'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ManifestoCaioTransportes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(null=True)),
                ('data_ultima_atualizacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('motorista_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operacional.motorista')),
                ('nota_fiscal_fk', models.ManyToManyField(to='operacional.nota_fiscal_caio_transportes')),
                ('usuario_cadastro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='criador_romaneio', to=settings.AUTH_USER_MODEL)),
                ('usuario_ultima_atualizacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atualizador_romaneio', to=settings.AUTH_USER_MODEL)),
                ('veiculo_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operacional.veiculo')),
            ],
        ),
    ]