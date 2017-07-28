# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 00:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfis', '0004_auto_20170719_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField()),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='perfis.Perfil')),
            ],
        ),
    ]
