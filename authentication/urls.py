# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

PARENT_PROJECT = "django2go."

urlpatterns = patterns('',
    # Example:
    (r'^$', PARENT_PROJECT + 'authentication.views.index'),
    (r'^access_denied$', PARENT_PROJECT + 'authentication.views.access_denied'),
    (r'^access_denied2$', PARENT_PROJECT + 'authentication.views.access_denied2'),
    (r'^login/$', PARENT_PROJECT + 'authentication.views.login_request'),
    (r'^logout/$', PARENT_PROJECT + 'authentication.views.logout_request'),
       
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)