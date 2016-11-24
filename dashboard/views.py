import simplejson
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from social_me import services as service
import datetime


@method_decorator(login_required, name='dispatch')
class MainProfileView(TemplateView):
    template_name = "dashboard/main_profile.html"

    def get(self, request, *args, **kwargs):

        facebook = service.check_for_social_media(request, 'facebook')
        instagram = service.check_for_social_media(request, 'instagram')
        linkedin = service.check_for_social_media(request, 'linkedin')
        spotify = service.check_for_social_media(request, 'spotify')

        return render(request, self.template_name, {'user': request.user})


@method_decorator(login_required, name='dispatch')
class SocialMe(TemplateView):
    template_name = "dashboard/social_me.html"
    current_date = datetime.date.today()

    def get(self, request, *args, **kwargs):
        # social media
        social = service.get_social_medias(request)

        # facebook
        facebook = service.check_for_social_media(request, 'facebook')
        facebook_places = service.get_tagged_places(facebook['auth_token'])
        facebook_likes_locations = service.get_likes_locations(facebook['auth_token'])
        print(facebook_likes_locations)

        # instagram
        instagram = service.check_for_social_media(request, 'instagram')
        instagram_locations = {}
        if service.check_for_social_media(request, 'instagram'):
            instagram_locations = service.get_media_locations(instagram['access_token'])

        return render(request, self.template_name, {'date': self.current_date,
                                                    'social': social,
                                                    'instagram_locations': instagram_locations,
                                                    'facebook_locations': facebook_places,
                                                    'facebook_locations_2': facebook_likes_locations,
                                                    })


@method_decorator(login_required, name='dispatch')
class FacebookDetailView(TemplateView):
    template_name = "dashboard/facebook_detail.html"

    def get(self, request, *args, **kwargs):
        if 'facebook' in request.session['social_media']:
            fb = request.session['social_media']['spotify']
            print("what is in session: {}".format(fb))
        return render(request, self.template_name, {'facebook': request.session['social_media']['facebook']})
