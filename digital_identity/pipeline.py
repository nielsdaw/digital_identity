from dashboard.models import FacebookProfile, InstagramProfile
from django.forms.models import model_to_dict
from digital_identity import services


def update_profile(strategy, backend, user, response, *args, **kwargs):

    if 'social_media' not in strategy.session:
        social_media_dict = {}
    else:
        social_media_dict = strategy.session_get('social_media')

    # Facebook
    if backend.name == 'facebook':
        print("facebook response: {}".format(response))

        # create new facebook dashboard, without storing to database
        facebook_profile = FacebookProfile.objects.create_facebook_profile(
            response.get('id'),
            response.get('first_name'),
            response.get('last_name'),
            response.get('email'),
            response.get('gender'),
            response['picture']['data']['url'],
            response['friends']['summary']['total_count'],
            response.get('link'),
            response['age_range']['min'],
            response.get('updated_time'),
            response.get('access_token')
        )
        # get correct size of profile picture
        facebook_profile.profile_picture_url = services.get_fb_photo_url(response.get('access_token'), 250, 250)

        # change it to dict, in order to set in session
        facebook_dict = model_to_dict(facebook_profile)

        # add facebook dict to social media dict
        social_media_dict.update({'facebook': facebook_dict})

    # Instagram
    elif backend.name == 'instagram':
        print("instagram response: {}".format(response))

        # create instagram object
        instagram_profile = InstagramProfile.objects.create_instagram_profile(
            response['user']['id'],
            response['user']['profile_picture'],
            response['user']['bio'],
            response['user']['website'],
            response['user']['username'],
            response['user']['full_name'],
            response['access_token'],
            response['data']['counts']['followed_by'],
            response['data']['counts']['media'],
            response['data']['counts']['follows']
        )
        # change it to dict, in order to set in session
        instagram_dict = model_to_dict(instagram_profile)

        # add instagram dict to social media dict
        social_media_dict.update({'instagram': instagram_dict})

    # LinkedIn
    elif backend.name == 'linkedin':
        print("LinkedIn response: {}".format(response))
        linkedin = {
            'l_first_name': response.get('firstName'),
            'l_industry': response.get('industry')
        }

        # add linkedin dict to social media dict
        social_media_dict.update({'linkedin': linkedin})

    print(social_media_dict)
    strategy.session_set('social_media', social_media_dict)
