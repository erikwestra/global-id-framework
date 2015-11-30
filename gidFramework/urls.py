""" gidFramework.urls

    This module defines the URL configuration for the GIDFramework system.
"""
from django.conf.urls import url, include
from django.conf import settings
import django.views.static

import gidFramework.website.views
import gidFramework.api.urls
import gidFramework.authentication.urls

urlpatterns = [
    url(r'^$',                gidFramework.website.views.main),
    url(r'^signup$',          gidFramework.website.views.signup),
    url(r'^signin$',          gidFramework.website.views.signin),
    url(r'^signout$',         gidFramework.website.views.signout),
    url(r'^why$',             gidFramework.website.views.why),
    url(r'^users$',           gidFramework.website.views.users),
    url(r'^stakeholders$',    gidFramework.website.views.stakeholders),
    url(r'^developers$',      gidFramework.website.views.developers),
    url(r'^team$',            gidFramework.website.views.team),
    url(r'^follow$',          gidFramework.website.views.follow),
    url(r'^contact$',         gidFramework.website.views.contact),
    url(r'^api/',             include(gidFramework.api.urls)),
    url(r'^auth/',            include(gidFramework.authentication.urls)),
    url(r'^admin$',           gidFramework.website.views.admin_main),
    url(r'^admin/names$',     gidFramework.website.views.admin_names),
    url(r'^admin/name/(?P<id>[0-9]+)',
                        gidFramework.website.views.admin_name),
    url(r'^admin/name/add$',  gidFramework.website.views.admin_name_add),
    url(r'^admin/name/find$', gidFramework.website.views.admin_name_find),
    url(r'^admin/name/delete/(?P<id>[0-9]+)',
                        gidFramework.website.views.admin_name_delete),
    url(r'^admin/check_availability$',
                        gidFramework.website.views.admin_check_availability),

    url(r'^static/(?P<path>.*)$', django.views.static.serve,
        {'document_root' : settings.STATICFILES_DIRS[0],
         'show_indexes'  : True}),
]

