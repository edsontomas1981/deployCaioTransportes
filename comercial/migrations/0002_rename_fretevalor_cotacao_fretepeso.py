# Generated by Django 4.0.6 on 2023-01-05 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cotacao',
            old_name='freteValor',
            new_name='fretePeso',
        ),
    ]
