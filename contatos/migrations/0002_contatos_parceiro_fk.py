# Generated by Django 4.0.6 on 2022-08-07 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parceiros', '0001_initial'),
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contatos',
            name='parceiro_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='parceiros.parceiros'),
        ),
    ]
