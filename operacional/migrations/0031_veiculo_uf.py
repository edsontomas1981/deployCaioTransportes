# Generated by Django 4.1.7 on 2024-02-14 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacional', '0030_marca_tipo_carroceria_tipo_combustivel_tipo_veiculo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='uf',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
