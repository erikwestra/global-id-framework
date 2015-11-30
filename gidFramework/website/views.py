""" gidFramework.website.views

    This module defines the views for the gidFramework.website application.
"""
import string

from django.http           import HttpResponse, HttpResponseRedirect
from django.shortcuts      import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from gidFramework.authentication import auth_controller
from gidFramework.shared.models  import *
from gidFramework.shared.lib     import nameChecker

#############################################################################

def main(request):
    """ Respond to our top-level "/" URL.
    """
    return render(request, "website/main.html",
                  {'cur_page' : "main"})

#############################################################################

def signup(request):
    """ Respond to our "/signup" URL.
    """
    return render(request, "website/not_yet.html",
                  {'cur_page' : "signup"})

#############################################################################

def signin(request):
    """ Respond to our "/signin" URL.
    """
    return render(request, "website/not_yet.html",
                  {'cur_page' : "signin"})

#############################################################################

def signout(request):
    """ Respond to our "/signout" URL.
    """
    return render(request, "website/not_yet.html",
                  {'cur_page' : "signout"})

#############################################################################

def why(request):
    """ Respond to our "/why" URL.
    """
    return render(request, "website/why.html",
                  {'cur_page' : "why"})

#############################################################################

def users(request):
    """ Respond to our "/users" URL.
    """
    return render(request, "website/not_yet.html",
                  {'cur_page' : "users"})

#############################################################################

def stakeholders(request):
    """ Respond to our "/stakeholders" URL.
    """
    return render(request, "website/not_yet.html",
                  {'cur_page' : "stakeholders"})

#############################################################################

def developers(request):
    """ Respond to our "/developers" URL.
    """
    return render(request, "website/not_yet.html",
                  {'cur_page' : "developers"})

#############################################################################

def team(request):
    """ Respond to our "/team" URL.
    """
    return render(request, "website/not_yet.html",
                  {'cur_page' : "team"})

#############################################################################

def follow(request):
    """ Respond to our "/follow" URL.
    """
    return render(request, "website/not_yet.html",
                  {'cur_page' : "follow"})

#############################################################################

def contact(request):
    """ Respond to our "/contact" URL.
    """
    return render(request, "website/not_yet.html",
                  {'cur_page' : "contact"})

#############################################################################

def admin_main(request):
    """ Respond to our "/admin" URL.

        We display a menu of available admin options.
    """
    if not auth_controller.is_logged_in(request):
        return HttpResponseRedirect(auth_controller.get_login_url())

    username            = auth_controller.get_username(request)
    can_edit_admins     = auth_controller.is_admin(request)
    edit_admins_url     = auth_controller.get_user_admin_url()
    change_password_url = auth_controller.get_change_password_url()
    logout_url          = auth_controller.get_logout_url()

    return render(request, "website/admin.html",
                  {'username'            : username,
                   'can_edit_admins'     : can_edit_admins,
                   'edit_admins_url'     : edit_admins_url,
                   'change_password_url' : change_password_url,
                   'logout_url'          : logout_url,
                  })

#############################################################################

def admin_names(request):
    """ Respond to our "/admin/names" URL.

        We display a paginated list of reserved names.
    """
    if not auth_controller.is_logged_in(request):
        return HttpResponseRedirect(auth_controller.get_login_url())

    if request.method == "GET":
        params = request.GET
    elif request.method == "POST":
        params = request.POST
    else:
        return HttpResponse("Bad HTTP Method")

    page = int(params.get("page", "1"))

    sorted_names = _get_sorted_names()
    paginator = Paginator(sorted_names, 10)

    if "show" in params:
        # We've been asked to show a given name.  Calculate the page number to
        # show.
        name_to_show = params['show']

        index = sorted_names.filter(name__lt=name_to_show).count()
        page = int(index/10) + 1

    # Show the desired page.

    try:
        names_in_page = paginator.page(page)
    except PageNotAnInteger:
        names_in_page = paginator.page(1)
    except EmptyPage:
        names_in_page = []

    return render(request, "website/reserved_names.html",
                  {'page'      : page,
                   'num_pages' : paginator.num_pages,
                   'names'     : names_in_page})

#############################################################################

def admin_name(request, id):
    """ Respond to the "/admin/name/XXX" URL.

        We display and let the user change the details of the given reserved
        name.
    """
    if not auth_controller.is_logged_in(request):
        return HttpResponseRedirect(auth_controller.get_login_url())

    try:
        reserved_name = ReservedName.objects.get(id=id)
    except ReservedName.DoesNotExist:
        return HttpResponse("No such name")

    err_name            = None # initially.
    err_twitter_sources = None # ditto.
    err_domain_sources  = None # ditto.

    if request.method == "GET":
        # We're displaying the form for the first time -> display the values
        # from the ReservedName record.
        name = reserved_name.name
        if reserved_name.twitter_sources != None:
            twitter_sources = reserved_name.twitter_sources
        else:
            twitter_sources = ""
        if reserved_name.domain_sources != None:
            domain_sources = reserved_name.domain_sources
        else:
            domain_sources = ""
    elif request.method == "POST":
        # The user is submitting the form.  Check the entered values.
        if request.POST.get("submit") == "save":
            name            = request.POST.get("name")
            twitter_sources = request.POST.get("twitter_sources")
            domain_sources  = request.POST.get("domain_sources")

            # Check the entered name.

            if name == "":
                err_name = "The reserved name cannot be blank."

            if err_name == None:
                if reserved_name.name != name:
                    # The user changed the name.  Make sure it's not already
                    # taken.
                    try:
                        existing_name = ReservedName.objects.get(name=name)
                    except ReservedName.DoesNotExist:
                        existing_name = None

                    if existing_name != None:
                        err_name = "That reserved name is already used."

            # Check the list of Twitter sources.

            valid_chars = string.ascii_letters + string.digits + ","

            twitter_sources = twitter_sources.replace(" ", "")
            for ch in twitter_sources:
                if ch not in valid_chars:
                    err_twitter_sources = "Invalid character '{}'".format(ch)

            if twitter_sources == "":
                twitter_sources = None

            # Check the list of domain sources.

            valid_chars = string.ascii_letters + string.digits + ",."

            domain_sources = domain_sources.replace(" ", "")
            for ch in domain_sources:
                if ch not in valid_chars:
                    err_domain_sources = "Invalid character '{}'".format(ch)

            if domain_sources == "":
                domain_sources = None

            # If there weren't any errors, save the updated name.

            if (err_name == None and err_twitter_sources == None
                                 and err_domain_sources == None):
                reserved_name.name            = name
                reserved_name.twitter_sources = twitter_sources
                reserved_name.domain_sources  = domain_sources
                reserved_name.save()
                return HttpResponseRedirect("/admin/names?show=" + name)
        elif request.POST.get("submit") == "cancel":
            return HttpResponseRedirect("/admin/names?show=" +
                                        reserved_name.name)
        elif request.POST.get("submit") == "delete":
            return HttpResponseRedirect("/admin/name/delete/" + id)

    # If we get here, display the form to the user.

    return render(request, "website/reserved_name.html",
                  {'name'                : name,
                   'twitter_sources'     : twitter_sources,
                   'domain_sources'      : domain_sources,
                   'err_name'            : err_name,
                   'err_twitter_sources' : err_twitter_sources,
                   'err_domain_sources'  : err_domain_sources,
                   'heading'             : "Edit Reserved Name",
                   'can_delete'          : True})

#############################################################################

def admin_name_add(request):
    """ Respond to the "/admin/name/add" URL.

        We let the user add a new reserved name.
    """
    if not auth_controller.is_logged_in(request):
        return HttpResponseRedirect(auth_controller.get_login_url())

    err_name            = None # initially.
    err_twitter_sources = None # ditto.
    err_domain_sources  = None # ditto.

    if request.method == "GET":
        # We're displaying the form for the first time -> set the default field
        # values.
        name            = ""
        twitter_sources = ""
        domain_sources  = ""
    elif request.method == "POST":
        # The user is submitting the form.  Check the entered values.
        if request.POST.get("submit") == "save":
            name            = request.POST.get("name")
            twitter_sources = request.POST.get("twitter_sources")
            domain_sources  = request.POST.get("domain_sources")

            # Check the entered name.

            if name == "":
                err_name = "The reserved name cannot be blank."

            if err_name == None:
                try:
                    existing_name = ReservedName.objects.get(name=name)
                except ReservedName.DoesNotExist:
                    existing_name = None

                if existing_name != None:
                    err_name = "That reserved name is already used."

            # Check the list of Twitter sources.

            valid_chars = string.ascii_letters + string.digits + ","

            twitter_sources = twitter_sources.replace(" ", "")
            for ch in twitter_sources:
                if ch not in valid_chars:
                    err_twitter_sources = "Invalid character '{}'".format(ch)

            if twitter_sources == "":
                twitter_sources = None

            # Check the list of domain sources.

            valid_chars = string.ascii_letters + string.digits + ",."

            domain_sources = domain_sources.replace(" ", "")
            for ch in domain_sources:
                if ch not in valid_chars:
                    err_domain_sources = "Invalid character '{}'".format(ch)

            if domain_sources == "":
                domain_sources = None

            # If there weren't any errors, save the updated name.

            if (err_name == None and err_twitter_sources == None
                                 and err_domain_sources == None):
                reserved_name = ReservedName()
                reserved_name.name            = name
                reserved_name.twitter_sources = twitter_sources
                reserved_name.domain_sources  = domain_sources
                reserved_name.save()
                return HttpResponseRedirect("/admin/names?show=" + name)
        elif request.POST.get("submit") == "cancel":
            return HttpResponseRedirect("/admin/names")

    # If we get here, display the form to the user.

    return render(request, "website/reserved_name.html",
                  {'name'                : name,
                   'twitter_sources'     : twitter_sources,
                   'domain_sources'      : domain_sources,
                   'err_name'            : err_name,
                   'err_twitter_sources' : err_twitter_sources,
                   'err_domain_sources'  : err_domain_sources,
                   'heading'             : "Add Reserved Name",
                   'can_delete'          : False})

#############################################################################

def admin_name_find(request):
    """ Respond to the "/admin/name/find" URL.

        We let the user find a reserved name.
    """
    if not auth_controller.is_logged_in(request):
        return HttpResponseRedirect(auth_controller.get_login_url())

    if request.method == "GET":
        # We're showing the form for the first time -> prepare our form
        # parameters.
        text    = ""
        err_msg = None
    elif request.method == "POST":
        if request.POST['submit'] == "search":
            text = request.POST['text']
            err_msg = None # initially.

            if text == "":
                err_msg = "You must enter some text to search for!"

            if err_msg == None:
                reserved_names = _get_sorted_names()
                results        = reserved_names.filter(name__istartswith=text)
                if len(results) == 0:
                    err_msg = "There are no names starting with this text."

            if err_msg == None:
                return HttpResponseRedirect("/admin/names?show=" +
                                            results[0].name)
        elif request.POST['submit'] == "cancel":
            return HttpResponseRedirect("/admin/names")

    # If we get here, show the "find" page to the user.

    return render(request, "website/find_name.html",
                  {'text'    : text,
                   'err_msg' : err_msg})

#############################################################################

def admin_name_delete(request, id):
    """ Respond to the "/admin/name/delete/XXX" URL.

        We let the user delete the reserved name with the given ID.
    """
    if not auth_controller.is_logged_in(request):
        return HttpResponseRedirect(auth_controller.get_login_url())

    try:
        reserved_name = ReservedName.objects.get(id=id)
    except ReservedName.DoesNotExist:
        return HttpResponse("No such name")

    if request.method == "POST" and request.POST['submit'] == "delete":
        # The user confirmed -> delete the name.
        reserved_name.delete()
        return HttpResponseRedirect("/admin/names")
    elif request.method == "POST" and request.POST['submit'] == "cancel":
        # The user cancelled.
        return HttpResponseRedirect("/admin/names?show=" + reserved_name.name)
    else:
        # Display the confirmation form.
        return render(request, "website/confirm_delete.html",
                      {'name'                : reserved_name.name})

#############################################################################

def admin_check_availability(request):
    """ Respond to the "/admin/check_availability" URL.

        We let the user enter a name, and see if that name is available.
    """
    if not auth_controller.is_logged_in(request):
        return HttpResponseRedirect(auth_controller.get_login_url())

    if request.method == "GET":
        # We're showing the form for the first time -> prepare our form
        # parameters.
        name     = ""
        response = None
    elif request.method == "POST":
        if request.POST['submit'] == "check":
            name = request.POST['name']
            response = None # initially.

            if name == "":
                response = "You must enter a name to check!"

            if response == None:
                if nameChecker.is_available(name):
                    response = "That name is available."
                else:
                    response = "Sorry, that name is taken."
        elif request.POST['submit'] == "done":
            return HttpResponseRedirect("/admin")

    # If we get here, show the "check availability" page to the user.

    return render(request, "website/check_availability.html",
                  {'name'     : name,
                   'response' : response})

#############################################################################
#                                                                           #
#                      P R I V A T E   F U N C T I O N S                    #
#                                                                           #
#############################################################################

def _get_sorted_names():
    """ Return a Django QuerySet representing the sorted list of names.
    """
    return ReservedName.objects.all().extra(
        select={'lower_name' : 'lower(name)'}).order_by("lower_name")

