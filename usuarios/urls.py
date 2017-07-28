from django.conf.urls import url
from usuarios.views import RegistrarUsuarioView, procurar
from django.contrib.auth import views
 
urlpatterns = [
	url(r'^registrar/$', RegistrarUsuarioView.as_view(), name='registrar'),
	url(r'^procurar/$', procurar, name='procurar'),
	url(r'^login/$', views.LoginView.as_view(template_name='login.html'), name='login'),
   	url(r'^logout/$', views.LogoutView.as_view(template_name='login.html'), name='logout'),
   	url(r'^password_change/$', views.PasswordChangeView.as_view(template_name='change_password.html'), name='change_password'),
]
