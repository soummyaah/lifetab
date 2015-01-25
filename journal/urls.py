from django.conf.urls import patterns, include, url
from views import *


# urlpatterns = patterns('',
# 	url(r'^create', EntryCreate, name="create"),
# 	url(r'^edit', EntryUpdate.as_view(), name="edit"),
# 	url(r'^delete', EntryDelete.as_view(), name="delete"),
# 	url(r'^list', EntryList.as_view(), name="list"),
# 	url(r'^show', EntryDetail.as_view(), name="future"),
# )

urlpatterns = patterns('',
	url(r'^create', entryCreate, name="create"),
	url(r'^edit', entryUpdate, name="edit"),
	url(r'^delete', entryDelete, name="delete"),
	url(r'^list', entryList, name="list"),
	url(r'^show', entryDetail, name="show"),
)