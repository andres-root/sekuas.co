from django.conf.urls.defaults import *

urlpatterns = patterns('apps.www.views',
	url(r'^add/post/$','add_post_view',name= "Vista_agregar_post"),
	url(r'^signup$','signup',name="signup_view"),
)

