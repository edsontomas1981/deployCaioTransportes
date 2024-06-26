# Generated by Django 4.1.7 on 2023-08-17 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operacional', '0018_nota_fiscal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frete_Dtc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalFrete', models.FloatField(default=0.0)),
                ('fretePeso', models.FloatField(default=0.0)),
                ('adValor', models.FloatField(default=0.0)),
                ('gris', models.FloatField(default=0.0)),
                ('despacho', models.FloatField(default=0.0)),
                ('outros', models.FloatField(default=0.0)),
                ('pedagio', models.FloatField(default=0.0)),
                ('vlrColeta', models.FloatField(default=0.0)),
                ('baseDeCalculo', models.FloatField(default=0.0)),
                ('aliquota', models.FloatField(default=0.0)),
                ('icmsRS', models.FloatField(default=0.0)),
                ('icmsIncluso', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=30, null=True)),
                ('observacao', models.CharField(max_length=70, null=True)),
                ('dataHora', models.DateTimeField(null=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_ultima_atualizacao', models.DateTimeField(auto_now=True)),
                ('dtc_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='frete_dtc', to='operacional.dtc')),
                ('usuario_cadastro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notas_fiscais_cadastradas_frete_dtc', to=settings.AUTH_USER_MODEL)),
                ('usuario_ultima_atualizacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notas_fiscais_atualizadas_frete_dtc', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
