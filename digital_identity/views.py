from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User



class Home(TemplateView):
    template_name = "index.html"

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated():
    #         return HttpResponseRedirect(reverse("home"))
    #     return super().get(request, *args, **kwargs)


def login(request):
    # LinkedIn settings
    if 'linkedin' in request.session:
        linked_in = request.session.get('linkedin')
        return render_to_response("index.html", {"user": request.user, 'linkedin': linked_in})
    else:
        return render_to_response("index.html", {"user": request.user})


@login_required
def logged(request):
    user = User.objects.get(pk=request.user.id)

    # LinkedIn settings
    if 'linkedin' in request.session:
        linked_in = request.session.get('linkedin')
        print(linked_in['l_industry'])
        return render_to_response("home.html", {"user": request.user,'linkedin':linked_in})
    else:
        return render_to_response("home.html", {"user": request.user})


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")
