# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from perfis.models import Perfil

class Post(models.Model):
	text = models.CharField(max_length=500, null=False)
	pub_date = models.DateField(auto_now_add=True)
	perfil =  models.ForeignKey(Perfil, related_name='posts')
	likes = models.IntegerField(default=0)
	imagem = models.FileField(null=True)


