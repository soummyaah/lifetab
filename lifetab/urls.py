from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lifetab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^$', 'lifetab.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^todo/', include('todos.urls', namespace='todo')),
    url(r'^journal/', include('journal.urls', namespace='journal')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
)
