# Generated by Django 4.0.6 on 2022-09-16 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operacional', '0008_coleta_impresso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coleta',
            name='dtc_fk',
        ),
        migrations.AddField(
            model_name='dtc',
            name='coleta_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coletaDtc', to='operacional.coleta'),
        ),
    ]
