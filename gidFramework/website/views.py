""" gidFramework.website.views

    This module defines the views for the gidFramework.website application.
"""
from django.http      import HttpResponse
from django.shortcuts import render

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

