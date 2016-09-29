from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.messages import get_messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import services



class Home(TemplateView):
    template_name = "index.html"

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated():
    #         return HttpResponseRedirect(reverse("home"))
    #     return super().get(request, *args, **kwargs)


def login(request):
    return render_to_response("index.html", {"user": request.user})


def login_error(request):
    pass


@login_required
def logged(request):
    response_dict = {"user": request.user}

    # Facebook dict
    if 'facebook' in request.session:
        facebook = request.session.get('facebook')
        response_dict.update({'facebook': facebook})

    if 'instagram' in request.session:
        instagram = request.session.get('instagram')
        recent_photos = services.get_recent_photos(instagram['access_token'])
        instagram.update({'photos': recent_photos})
        response_dict.update({'instagram': instagram})

    # LinkedIn dict
    if 'linkedin' in request.session:
        linked_in = request.session.get('linkedin')
        response_dict.update({'linkedin': linked_in})

    return render_to_response("home.html", response_dict)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")
