# Generated by Django 4.1.7 on 2024-03-30 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operacional', '0045_manifesto_contrato_fk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato',
            name='numero_carta_frete',
        ),
    ]
