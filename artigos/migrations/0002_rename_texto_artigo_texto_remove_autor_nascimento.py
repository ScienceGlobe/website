# Generated by Django 5.0.4 on 2024-05-03 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artigo',
            old_name='Texto',
            new_name='texto',
        ),
        migrations.RemoveField(
            model_name='autor',
            name='nascimento',
        ),
    ]
