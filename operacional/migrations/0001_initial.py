# Generated by Django 4.0.6 on 2022-08-26 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parceiros', '0001_initial'),
        ('enderecos', '0002_enderecos_complemento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.IntegerField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=7)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9)),
                ('cubM3', models.DecimalField(decimal_places=2, max_digits=7)),
                ('veiculo', models.CharField(max_length=50)),
                ('especie', models.CharField(max_length=50)),
                ('observacao', models.CharField(max_length=150)),
                ('nome', models.CharField(max_length=15)),
                ('contato', models.CharField(max_length=20)),
                ('consignatario_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consigColeta', to='parceiros.parceiros')),
                ('destinatario_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destColeta', to='parceiros.parceiros')),
                ('endereco_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endColeta', to='enderecos.enderecos')),
                ('redespacho_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='redespColeta', to='parceiros.parceiros')),
                ('remetente_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remetColeta', to='parceiros.parceiros')),
            ],
        ),
    ]
