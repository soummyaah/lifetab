from django.conf.urls import patterns, include, url
from views import *


urlpatterns = patterns('',
	url(r'^create', , name="create"),
	url(r'^edit', , name="edit"),
	url(r'^delete', , name="delete"),
	url(r'^list', , name="list"),
	url(r'^archived', , name="future"),
	url(r'^show/(?<pk>[0-9]+)', , name="future"),
)