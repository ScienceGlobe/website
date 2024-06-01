# Generated by Django 5.0.4 on 2024-04-22 21:50

import django.db.models.deletion
import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('nascimento', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Insira um tipo de artigo', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('Texto', models.TextField(help_text='Insira o texto do artigo', max_length=4000)),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='artigos.autor')),
            ],
        ),
        migrations.AddConstraint(
            model_name='tipo',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='tipo_name_case_insensitive_unique', violation_error_message='Esse tipo ja existe (case insensitive match)'),
        ),
        migrations.AddField(
            model_name='artigo',
            name='tipo',
            field=models.ForeignKey(help_text='Selecione o tipo do artigo', on_delete=django.db.models.deletion.RESTRICT, to='artigos.tipo'),
        ),
    ]
