""" gidFramework.urls

    This module defines the URL configuration for the GIDFramework system.
"""
from django.conf.urls import url
import gidFramework.website.views

urlpatterns = [
    url(r'^$', gidFramework.website.views.main)
]

