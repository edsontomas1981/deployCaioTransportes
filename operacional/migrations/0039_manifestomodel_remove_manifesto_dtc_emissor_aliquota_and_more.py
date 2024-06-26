# Generated by Django 4.1.7 on 2024-03-20 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operacional', '0038_dtcmanifesto_manifesto_dtcmanifesto_manifesto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManifestoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_previsão_inicio', models.DateTimeField(null=True)),
                ('data_previsão_chegada', models.DateTimeField(null=True)),
                ('frete_carreteiro', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('frete_adiantamento', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('lacres', models.CharField(max_length=100, null=True)),
                ('averbacao', models.CharField(max_length=20, null=True)),
                ('liberacao', models.CharField(max_length=20, null=True)),
                ('observacao', models.TextField(null=True)),
                ('data_cadastro', models.DateTimeField(null=True)),
                ('data_ultima_atualizacao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='manifesto',
            name='dtc',
        ),
        migrations.AddField(
            model_name='emissor',
            name='aliquota',
            field=models.IntegerField(default=7),
        ),
        migrations.AddField(
            model_name='emissor',
            name='sigla_filial',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='manifesto',
            name='ocorrencia_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='operacional.ocorrencia_manifesto'),
        ),
        migrations.AlterField(
            model_name='manifesto',
            name='motoristas',
            field=models.ManyToManyField(to='operacional.motorista'),
        ),
        migrations.AlterField(
            model_name='manifesto',
            name='veiculos',
            field=models.ManyToManyField(to='operacional.veiculo'),
        ),
        migrations.DeleteModel(
            name='DtcManifesto',
        ),
        migrations.AddField(
            model_name='manifestomodel',
            name='emissor_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operacional.emissor'),
        ),
        migrations.AddField(
            model_name='manifestomodel',
            name='motoristas',
            field=models.ManyToManyField(to='operacional.motorista'),
        ),
        migrations.AddField(
            model_name='manifestomodel',
            name='ocorrencia_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='operacional.ocorrencia_manifesto'),
        ),
        migrations.AddField(
            model_name='manifestomodel',
            name='rota_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='operacional.rota'),
        ),
        migrations.AddField(
            model_name='manifestomodel',
            name='usuario_cadastro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='criador_manifesto_model', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='manifestomodel',
            name='usuario_ultima_atualizacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atualizador_manifesto_model', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='manifestomodel',
            name='veiculos',
            field=models.ManyToManyField(to='operacional.veiculo'),
        ),
    ]
