# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from posts.models import Post
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.
def post(request):
	form = PostForm(request.POST, request.FILES)
		
	if form.is_valid():
		imagem = handle_uploaded_file(request.FILES['imagem'])

		perfil = request.user.perfil
		post = Post.objects.create(text=form.data['text'], perfil=perfil, imagem=imagem)

		post.save()
	
		return redirect('index')

	return redirect('index')

def handle_uploaded_file(imagem):
	fs = FileSystemStorage()
	filename = fs.save(imagem.name, imagem)
	uploaded_file_url = fs.url(filename)
	return uploaded_file_url

def like(request, post_id):
	post = Post.objects.get(id=post_id)
	post.likes = post.likes+1
	post.save()

	return redirect('index')

def delete(request, post_id):
	post = Post.objects.get(id=post_id)
	
	if request.user.perfil.id == post.perfil.id:
		post.delete()

	return redirect('index')	

