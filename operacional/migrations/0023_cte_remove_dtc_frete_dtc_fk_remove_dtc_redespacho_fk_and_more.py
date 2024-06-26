# Generated by Django 4.2.3 on 2023-08-23 00:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comercial', '0014_alter_cotacao_tabela_fk'),
        ('operacional', '0022_alter_dtc_data_cadastro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origem_cte', models.CharField(max_length=5, null=True)),
                ('destino_cte', models.CharField(max_length=5, null=True)),
                ('emissora_cte', models.CharField(max_length=5, null=True)),
                ('tipo_cte', models.CharField(max_length=5, null=True)),
                ('cfop_cte', models.CharField(max_length=5, null=True)),
                ('redesp_cte', models.CharField(max_length=5, null=True)),
                ('tipo_calculo_cte', models.CharField(max_length=5, null=True)),
                ('observacao', models.CharField(max_length=70, null=True)),
                ('icms_incluso', models.BooleanField()),
                ('frete_calculado', models.FloatField(default=0.0)),
                ('advalor', models.FloatField(default=0.0)),
                ('gris', models.FloatField(default=0.0)),
                ('despacho', models.FloatField(default=0.0)),
                ('outros', models.FloatField(default=0.0)),
                ('pedagio', models.FloatField(default=0.0)),
                ('vlr_coleta', models.FloatField(default=0.0)),
                ('base_de_calculo', models.FloatField(default=0.0)),
                ('aliquota', models.FloatField(default=0.0)),
                ('icms_valor', models.FloatField(default=0.0)),
                ('total_frete', models.FloatField(default=0.0)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_ultima_atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='dtc',
            name='frete_dtc_fk',
        ),
        migrations.RemoveField(
            model_name='dtc',
            name='redespacho_fk',
        ),
        migrations.DeleteModel(
            name='Frete_Dtc',
        ),
        migrations.AddField(
            model_name='cte',
            name='dtc_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='frete_dtc', to='operacional.dtc'),
        ),
        migrations.AddField(
            model_name='cte',
            name='tabela_frete',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coletaDtc', to='comercial.tabelafrete'),
        ),
        migrations.AddField(
            model_name='cte',
            name='usuario_cadastro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cadastrado_dtc', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cte',
            name='usuario_ultima_atualizacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alterou_dtc', to=settings.AUTH_USER_MODEL),
        ),
    ]
