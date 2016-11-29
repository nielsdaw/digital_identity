from dashboard.models import FacebookProfile, InstagramProfile, LinkedinProfile, SpotifyProfile
from django.forms.models import model_to_dict
from social_me import services


def update_profile(strategy, backend, user, response, *args, **kwargs):
    """
    :param strategy: current strategy
    :param backend: backend
    :param user: current user
    :param response: the response
    :param args: self said
    :param kwargs: u know
    """

    if 'social_media' not in strategy.session:
        social_media_dict = {}
    else:
        social_media_dict = strategy.session_get('social_media')


    # Facebook
    if backend.name == 'facebook':
        print("facebook response: {}".format(response))
        relationship = 'Not public'
        hometown = 'Not public'
        location = "Not public"
        devices = "SmartPhone"

        if 'relationship_status' in response:
            relationship = response.get('relationship_status')

        if 'hometown' in response:
            hometown = response.get('hometown')['name']

        if 'location' in response:
            location = response.get('location')['name']

        if 'devices' in response:
            devices = response['devices'][0]['hardware']


            # instantiate new facebook dashboard, without storing to database
        facebook_profile = FacebookProfile.objects.create_facebook_profile(
            response.get('id'),
            response.get('first_name'),
            response.get('last_name'),
            response.get('birthday'),
            relationship,
            hometown,
            location,
            response.get('email'),
            response.get('gender'),
            response['picture']['data']['url'],
            response['friends']['summary']['total_count'],
            response.get('link'),
            response['age_range']['min'],
            response.get('updated_time'),
            response.get('access_token'),
            devices
        )

        # get correct size of profile picture
        facebook_profile.profile_picture_url = services.get_fb_photo_url(response.get('access_token'), 250, 250)

        # change it to dict, in order to set in session
        facebook_dict = model_to_dict(facebook_profile)

        # add facebook dict to social media dict
        social_media_dict.update({'facebook': facebook_dict})

    # Instagram
    elif backend.name == 'instagram':
        # print("instagram response: {}".format(response))

        # instantiate instagram object
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

        # instantiate linkedin object
        linkedin_profile = LinkedinProfile.objects.create_linkedin_profile(
            response['firstName'],
            response['lastName'],
            response['emailAddress'],
            response['headline'],
            response['industry'],
            response['location']['name'],
            response['currentShare']['content']['title'],
            response['numConnections'],
            response['summary'] if 'summary' in response else "",
            response['specialties'] if 'specialities' in response else "",
            response['positions']['_total'],
            response['pictureUrls']['values'][0]
        )

        # change it to dict, in order to set in session
        linkedin_dict = model_to_dict(linkedin_profile)

        # add linkedin dict to social media dict
        social_media_dict.update({'linkedin': linkedin_dict})



    # Spotify
    elif backend.name == 'spotify':
        print("spotify response: {}".format(response))

        spotify_profile = SpotifyProfile.objects.create_spotify_profile(
            response['display_name'],
            response['email'],
            response['followers']['total'],
            response['access_token'],
            response['images'][0]['url']
        )
        # change it to dict, in order to set in session
        spotify_dict = model_to_dict(spotify_profile)

        # add linkedin dict to social media dict
        social_media_dict.update({'spotify': spotify_dict})


    #update social media in session
    strategy.session_set('social_media', social_media_dict)
