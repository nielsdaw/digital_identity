from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from digital_identity import services


# Create your views here.
@login_required
def main_profile(request):
    response_dict = {"user": request.user}

    # Facebook dict
    if 'facebook' in request.session:
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

    return render_to_response("social_profile/main_profile.html", response_dict)