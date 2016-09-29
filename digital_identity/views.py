from django.shortcuts import render, render_to_response
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy, reverse
from django.views import generic
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from . import services


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        print("Index get visited")
        return render(request, self.template_name,)


@method_decorator(login_required, name='dispatch')
class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        print(self.request.session)
        return context

    # get request
    def get(self, request, *args, **kwargs):
        response_dict = {"user": request.user}

        # Facebook dict
        if 'facebook' in request.session:
            print("facebook detected")
            facebook = request.session.get('facebook')
            response_dict.update({'facebook': facebook})

        # Instagram dict
        if 'instagram' in request.session:
            instagram = request.session.get('instagram')
            recent_photos = services.get_recent_photos(instagram['access_token'])
            instagram.update({'photos': recent_photos})
            response_dict.update({'instagram': instagram})

        # LinkedIn dict
        if 'linkedin' in request.session:
            linked_in = request.session.get('linkedin')
            response_dict.update({'linkedin': linked_in})

        return render(request, self.template_name, response_dict)


class LoginView(TemplateView):
    template_name = "registration/login.html"

    def get(self, request, *args, **kwargs):
        print("Login get visited get")
        return render(request, self.template_name,)


@method_decorator(login_required, name='dispatch')
class LogoutView(generic.RedirectView):
    url = reverse_lazy("index")

    def get(self, request, *args, **kwargs):
        print("Logout view visited")
        messages.add_message(request, messages.SUCCESS, 'Logged out successfully - see you soon.')
        logout(request)
        return super().get(request, *args, **kwargs)
