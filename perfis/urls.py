from django.conf.urls import url
from perfis import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^perfil/(?P<perfil_id>\d+)$', views.exibir, name='exibir'),
	url(r'^perfil/(?P<perfil_id>\d+)/convidar$', views.convidar, name='convidar'),
	url(r'^convite/(?P<convite_id>\d+)/aceitar$', views.aceitar, name='aceitar'),
	url(r'^perfil/(?P<perfil_id>\d+)/bloquear$', views.bloquear, name='bloquear'),
	url(r'^perfil/(?P<perfil_id>\d+)/desbloquear$', views.desbloquear, name='desbloquear'),
	# url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT})
] 