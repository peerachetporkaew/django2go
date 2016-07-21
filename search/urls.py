# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # (r'^django2go/', include('django2go.foo.urls')),
    (r'^index$' ,'django2go.search.views.index'),
)