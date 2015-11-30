""" gidFramework.shared.lib.nameChecker

    This module implements the generic behaviour of checking to see if a given
    name has been reserved.
"""
import string

from gidFramework.shared.models import *

#############################################################################

def is_available(name):
    """ Return True if and only if the given name is available.
    """
    stripped_name = []
    for ch in name:
        if ch in string.ascii_letters + string.digits:
            stripped_name.append(ch)
    stripped_name = "".join(stripped_name)

    try:
        reserved_name = ReservedName.objects.get(name__iexact=stripped_name)
    except ReservedName.DoesNotExist:
        reserved_name = None

    return (reserved_name == None)

