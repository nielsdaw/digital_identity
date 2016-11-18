from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from digital_identity import services as service
import datetime


@method_decorator(login_required, name='dispatch')
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
        if 'spotify' in request.session['social_media']:
            fb = request.session['social_media']['spotify']
            print("what is in session: {}".format(fb))
        return render(request, self.template_name, {'user': request.user})


@method_decorator(login_required, name='dispatch')
class SocialMe(TemplateView):
    template_name = "dashboard/social_me.html"
    current_date = datetime.date.today()

    def get(self, request, *args, **kwargs):

        social = request.session['social_media']
        print("what is in social: {}".format(social))

        return render(request, self.template_name, {'date': self.current_date, 'social': social})


@method_decorator(login_required, name='dispatch')
class FacebookDetailView(TemplateView):
    template_name = "dashboard/facebook_detail.html"

    def get(self, request, *args, **kwargs):
        if 'facebook' in request.session['social_media']:
            fb = request.session['social_media']['spotify']
            print("what is in session: {}".format(fb))
        return render(request, self.template_name, {'facebook': request.session['social_media']['facebook']})
