from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	nome = models.CharField(max_length=255, null=False)
	telefone = models.CharField(max_length=15, null=False)
	nome_empresa = models.CharField(max_length=255, null=False)
	contatos = models.ManyToManyField('self')
	contatos_bloqueados = models.ManyToManyField('self')
	usuario = models.OneToOneField(User, related_name='perfil')
	imagem = models.FileField(null=True)

	@property
	def email(self):
		return self.usuario.email

	def convidar(self, perfil_convidado):
		Convite(solicitante=self, convidado=perfil_convidado).save()
		#convite = Convite(solicitante=self, convidado=perfil_convidado)
		#convite.save()

	def bloquear(self, perfil):
		self.contatos_bloqueados.add(perfil)
		self.contatos.remove(perfil)
		perfil.contatos.remove(self)

	def desbloquear(self, perfil):
		self.contatos_bloqueados.remove(perfil)
		self.contatos.add(perfil)
		perfil.contatos.add(self)

class Convite(models.Model):
	solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
	convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')

	def aceitar(self):
		self.convidado.contatos.add(self.solicitante)
		self.solicitante.contatos.add(self.convidado)
		self.delete()


