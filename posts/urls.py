from django.conf.urls import url
from posts import views

urlpatterns = [
	url(r'^post$', views.post, name='post'),
	url(r'^post/(?P<post_id>\d+)/deletar$', views.delete, name='delete_post'),
	url(r'^post/(?P<post_id>\d+)/like$', views.like, name='like')
] 