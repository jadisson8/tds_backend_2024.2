# Generated by Django 5.1.5 on 2025-01-22 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Equipe',
                'verbose_name_plural': 'Equipes',
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=1000, verbose_name='Descrição')),
                ('dt_inicial', models.DateField()),
                ('dt_final', models.DateField()),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
                'ordering': ['dt_final'],
            },
        ),
        migrations.CreateModel(
            name='Membro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('inscricao', models.PositiveIntegerField(verbose_name='Inscrição')),
                ('sexo', models.CharField(choices=[('M', 'Mulher'), ('H', 'Homem')], max_length=1)),
                ('email', models.EmailField(max_length=100)),
                ('funcao', models.CharField(max_length=32, verbose_name='Função')),
                ('equipe', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='membros', to='core.equipe')),
            ],
            options={
                'verbose_name': 'Membro',
                'verbose_name_plural': 'Membros',
                'ordering': ['equipe__nome', 'nome', 'inscricao'],
            },
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=1000, verbose_name='Descrição')),
                ('feito', models.BooleanField(default=False)),
                ('dt_limite', models.DateField()),
                ('membro', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='atividades', to='core.membro')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='atividades', to='core.projeto')),
            ],
            options={
                'verbose_name': 'Atividade',
                'verbose_name_plural': 'Atividades',
                'ordering': ['projeto__nome', 'nome'],
            },
        ),
    ]
