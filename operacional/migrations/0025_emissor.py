# Generated by Django 4.1.7 on 2023-12-11 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0003_municipios'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operacional', '0024_alter_cte_data_cadastro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emissor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=14)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('inscricao_estadual', models.CharField(max_length=20)),
                ('regime_tributario', models.CharField(max_length=50)),
                ('data_cadastro', models.DateTimeField(null=True)),
                ('data_ultima_atualizacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('endereco_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enderecos.enderecos')),
                ('usuario_cadastro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='criador_emissor', to=settings.AUTH_USER_MODEL)),
                ('usuario_ultima_atualizacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atualizador_emissor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
