from django.conf.urls import patterns, include, url
from views import *


urlpatterns = patterns('',
	url(r'^create', , name="create"),
	url(r'^edit', , name="edit"),
	url(r'^delete', , name="delete"),
	url(r'^done', , name="done"),
	url(r'^today', , name="today"),
	url(r'^future', , name="future"),
)