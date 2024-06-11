# Generated by Django 4.1.7 on 2024-02-18 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacional', '0034_motorista_dt_emissao_cnh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorista',
            name='cnh_numero',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='motorista',
            name='estado_civil',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='motorista',
            name='numero_registro_cnh',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='motorista',
            name='pis',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
