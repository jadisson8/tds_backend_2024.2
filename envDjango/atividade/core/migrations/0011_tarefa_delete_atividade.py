# Generated by Django 5.1.5 on 2025-01-22 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_membro_sexo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=1000, verbose_name='Descrição')),
                ('concluido', models.BooleanField(default=False, verbose_name='Concluído?')),
                ('dt_limite', models.DateField(verbose_name='Data limite')),
                ('membro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tarefas', to='core.membro')),
                ('proejto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tarefas', to='core.projeto')),
            ],
            options={
                'verbose_name': 'Tarefa',
                'verbose_name_plural': 'Tarefas',
                'ordering': ['dt_limite', 'concluido', 'nome'],
            },
        ),
        migrations.DeleteModel(
            name='Atividade',
        ),
    ]
