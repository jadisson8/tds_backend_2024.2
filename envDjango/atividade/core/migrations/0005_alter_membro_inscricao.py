# Generated by Django 5.1.5 on 2025-01-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_atividade_dt_limite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='inscricao',
            field=models.PositiveBigIntegerField(verbose_name='Inscrição'),
        ),
    ]
