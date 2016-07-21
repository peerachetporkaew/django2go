# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

project_name = "app"

urlpatterns = patterns('',
    # Example:
    # (r'^django2go/', include('django2go.foo.urls')),
    (r'^app/webbuilder/',include('django2go.webbuilder.urls')),
    (r'^app/authentication/',include('django2go.authentication.urls')),    
    (r'^app/search/',include('django2go.search.urls')),
    (r'^app/admin/logout/',  'django2go.authentication.views.index'),
    (r'^app/admin/', include(admin.site.urls)),
)