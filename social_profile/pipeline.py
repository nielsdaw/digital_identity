from social_profile.models import FacebookProfile, InstagramProfile
from django.forms.models import model_to_dict


def update_profile(strategy, backend, user, response, *args, **kwargs):

    # Facebook
    if backend.name == 'facebook':
        print("facebook response: {}".format(response))

        # create new facebook profile, without storing to database
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
        # change it to dict, in order to set in session
        facebook_dict = model_to_dict(facebook_profile)

        # add facebook dict to session
        strategy.session_set('facebook', facebook_dict)

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

        # add facebook dict to session
        strategy.session_set('instagram', instagram_dict)

    # LinkedIn
    elif backend.name == 'linkedin':
        print("LinkedIn response: {}".format(response))
        linkedin = {
            'l_first_name': response.get('firstName'),
            'l_industry': response.get('industry')
        }
        strategy.session_set('linkedin', linkedin)


