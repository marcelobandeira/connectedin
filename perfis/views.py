
# dentro das funcoes de view, sempre deve ter um request como parametro

from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite
from posts.models import Post
from perfis.forms import ImagemForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	perfis = Perfil.objects.all()
	perfil_logado = get_perfil_logado(request)
	lista = []
	contatos = perfil_logado.contatos.values('id')
	for c in contatos:
		lista.append(c['id'])

	lista.append(perfil_logado.id)
	posts = Post.objects.filter(perfil__in=lista).order_by('-id')
	
	return render(request, 'index.html', {'perfis' : perfis, 
										'perfil_logado' : perfil_logado, 
										'posts': posts})

@login_required
def exibir(request, perfil_id):

	perfil = Perfil.objects.get(id = perfil_id)
	perfil_logado = get_perfil_logado(request)
	ja_he_contato = perfil in perfil_logado.contatos.all()
	bloqueado = perfil in perfil_logado.contatos_bloqueados.all()
	return render(request, 'perfil.html', { "perfil" : perfil, 
											"ja_he_contato" : ja_he_contato,
											"bloqueado": bloqueado })

@login_required
def convidar(request, perfil_id):
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_a_convidar)
	return redirect('index') #vai para a funcao de view index

@login_required
def aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')

@login_required
def get_perfil_logado(request):
	#return Perfil.objects.get(id=1)
	return request.user.perfil

def bloquear(request, perfil_id):
	perfil_a_bloquear = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.bloquear(perfil_a_bloquear)
	return redirect('index')

def desbloquear(request, perfil_id):
	perfil_a_desbloquear = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.desbloquear(perfil_a_desbloquear)
	return redirect('index')

def imagem(request):
	form = ImagemForm(request.POST, request.FILES)
		
	if form.is_valid():
		imagem = handle_uploaded_file(request.FILES['imagem'])

		perfil = request.user.perfil
		perfil.imagem = imagem
		
		perfil.save()
	
		return redirect('index')

	return redirect('index')

def handle_uploaded_file(imagem):
	fs = FileSystemStorage()
	filename = fs.save(imagem.name, imagem)
	uploaded_file_url = fs.url(filename)
	return uploaded_file_url
