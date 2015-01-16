from django.conf.urls import patterns, include, url
from views import *


urlpatterns = patterns('',
	url(r'^create', EntryCreate.as_view(), name="create"),
	url(r'^edit', EntryUpdate.as_view(), name="edit"),
	url(r'^delete', EntryDelete.as_view(), name="delete"),
	url(r'^list', EntryList.as_view(), name="list"),
	url(r'^show', EntryDetail.as_view(), name="future"),
)