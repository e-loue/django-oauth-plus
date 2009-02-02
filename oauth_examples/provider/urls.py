from django.conf.urls.defaults import *
from django.contrib import admin

from oauth_provider.views import protected_resource_example

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^oauth/', include('oauth_provider.urls')),
    url(r'^oauth/photo/$', protected_resource_example, name='oauth_example'),
    (r'^admin/(.*)', admin.site.root),
)
