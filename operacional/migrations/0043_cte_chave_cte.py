# Generated by Django 4.1.7 on 2024-03-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacional', '0042_alter_dtcmanifesto_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='cte',
            name='chave_cte',
            field=models.CharField(max_length=44, null=True),
        ),
    ]
