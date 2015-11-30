""" gidFramework.api.views

    This module defines the various view functions for the "api" application.
"""
import json

from django.http import HttpResponse

from gidFramework.shared.lib import nameChecker

#############################################################################

def is_reserved(request, name):
    """ Implement the 'api/is_reserved' endpoint.
    """
    available = nameChecker.is_available(name)

    if available:
        response = {'reserved' : False}
    else:
        response = {'reserved' : True}

    return HttpResponse(json.dumps(response),
                        content_type="application/json")

