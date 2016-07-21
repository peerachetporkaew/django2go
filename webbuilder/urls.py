# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # (r'^django2go/', include('django2go.foo.urls')),

    (r'^index$' ,'django2go.webbuilder.views.index'),
    (r'^page$' ,'django2go.webbuilder.views.page'),
    (r'^load/','django2go.webbuilder.views.load'),
    (r'^save_file/','django2go.webbuilder.views.save_file'),
    (r'^save_file3','django2go.webbuilder.views.save_file3'),
    (r'^run/','django2go.webbuilder.views.run'),
    (r'^upload_file/','django2go.webbuilder.views.upload_file'),
    (r'^del_file/','django2go.webbuilder.views.del_file'),
    (r'^new_folder/','django2go.webbuilder.views.new_folder'),
    (r'^new_file/','django2go.webbuilder.views.new_file'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)