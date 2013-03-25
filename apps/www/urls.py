from django.conf.urls.defaults import *

urlpatterns = patterns('apps.www.views',
	url(r'^add/post/$','add_post_view',name= "Vista_agregar_post"),
	url(r'^signup$','signup',name="signup_view"),
	url(r'^photos$','photos',name="photos_view"),
	url(r'^bio$','bio',name="bio_view"),
	url(r'^disco$','disco',name="disco_view"),
	url(r'^config.xml$','config_xml',name="config_xml_view"),

)

