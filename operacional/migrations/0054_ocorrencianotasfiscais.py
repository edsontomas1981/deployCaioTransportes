# Generated by Django 5.0.6 on 2024-06-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacional', '0053_nota_fiscal_caio_transportes_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OcorrenciaNotasFiscais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocorrencia', models.CharField(max_length=70)),
            ],
        ),
    ]
