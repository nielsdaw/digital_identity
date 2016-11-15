from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from digital_identity import services as service


class MainProfileView(TemplateView):
    template_name = "dashboard/main_profile.html"

    def get(self, request, *args, **kwargs):
        if 'instagram' in request.session['social_media']:
            fb = request.session['social_media']['instagram']
            print("what is in session: {}".format(fb))
        if 'facebook' in request.session['social_media']:
            fb = request.session['social_media']['facebook']
            print("what is in session: {}".format(fb))
        if 'linkedin' in request.session['social_media']:
            fb = request.session['social_media']['linkedin']
            print("what is in session: {}".format(fb))
        return render(request, self.template_name, {'user': request.user})


class SocialMe(TemplateView):
    template_name = "dashboard/social_me.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'user': request.user})


class FacebookDetailView(TemplateView):
    template_name = "dashboard/facebook_detail.html"

    def get(self, request, *args, **kwargs):
        if 'facebook' in request.session['social_media']:
            fb = request.session['social_media']['facebook']
            print("what is in session: {}".format(fb))
        return render(request, self.template_name, {'facebook': request.session['social_media']['facebook']})
