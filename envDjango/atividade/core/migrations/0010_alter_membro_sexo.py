# Generated by Django 5.1.5 on 2025-01-22 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_equipe_options_equipe_ativa_projeto_equipe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='sexo',
            field=models.CharField(blank=True, choices=[('M', 'Mulher'), ('H', 'Homem')], max_length=1, null=True),
        ),
    ]
