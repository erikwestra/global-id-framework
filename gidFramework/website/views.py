""" gidFramework.website.views

    This module defines the views for the gidFramework.website application.
"""
from django.http import HttpResponse

#############################################################################

def main(request):
    """ Respond to our top-level "/" URL.
    """
    return HttpResponse("Hello world!")

