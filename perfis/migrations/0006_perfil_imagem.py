# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-13 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0005_perfil_contatos_bloqueados'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='imagem',
            field=models.FileField(null=True, upload_to=b''),
        ),
    ]