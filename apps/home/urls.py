from django.conf.urls.defaults import *

urlpatterns = patterns('apps.home.views',
	url(r'^$','index_view',name='vista_principal'),
	url(r'^contacto/$','contact_view',name='vista_contacto'),
	url(r'^login/$','login_view',name= "vista_login"),
	url(r'^logout/$','logout_view',name= "vista_logout"),
)
