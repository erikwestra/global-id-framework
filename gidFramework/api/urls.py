""" gidFramework.api.urls

    This module defines the URL configuration for the "api" application.
"""
from django.conf.urls import url

import gidFramework.api.views

urlpatterns = [
    url(r'^is_reserved/(?P<name>.*)$', gidFramework.api.views.is_reserved),
]


