# Generated by Django 5.0.6 on 2024-06-12 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacional', '0050_nota_fiscal_caio_transportes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota_fiscal_caio_transportes',
            name='natureza',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='nota_fiscal_caio_transportes',
            name='peso',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='nota_fiscal_caio_transportes',
            name='volume',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
