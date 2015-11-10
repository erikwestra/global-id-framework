""" gidFramework.urls

    This module defines the URL configuration for the GIDFramework system.
"""
from django.conf.urls import url
from django.conf import settings
import django.views.static

import gidFramework.website.views

urlpatterns = [
    url(r'^$',             gidFramework.website.views.main),
    url(r'^signup$',       gidFramework.website.views.signup),
    url(r'^signin$',       gidFramework.website.views.signin),
    url(r'^signout$',      gidFramework.website.views.signout),
    url(r'^why$',          gidFramework.website.views.why),
    url(r'^users$',        gidFramework.website.views.users),
    url(r'^stakeholders$', gidFramework.website.views.stakeholders),
    url(r'^developers$',   gidFramework.website.views.developers),
    url(r'^team$',         gidFramework.website.views.team),
    url(r'^follow$',       gidFramework.website.views.follow),
    url(r'^contact$',      gidFramework.website.views.contact),

    url(r'^static/(?P<path>.*)$', django.views.static.serve,
        {'document_root' : settings.STATICFILES_DIRS[0],
         'show_indexes'  : True}),
]

