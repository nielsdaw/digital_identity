from social_profile.models import UserProfile, FacebookProfile
from django.forms.models import model_to_dict

def update_profile(strategy, backend, user, response, *args, **kwargs):
    profile = ""

    # Facebook
    if backend.name == 'facebook':
        profile = UserProfile.objects.get(user=user)
        print("facebook response: {}".format(response))
        profile.facebook_id = response.get('id')
        profile.facebook_username = response.get('name')
        profile.photo_url = response['picture']['data']['url']
        profile.save()

        var = "{},\n{},\n{},\n{},\n{},\n{},\n{},\n{},\n{},\n{}".format(
            response.get('id'),
            response.get('first_name'),
            response.get('last_name'),
            response.get('email'),
            response.get('gender'),
            response['picture']['data']['url'],
            response['friends']['summary']['total_count'],
            response.get('link'),
            response.get('age_range'),
            response.get('updated_time')
        )
        print(var)

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
            response.get('updated_time')
        )

        data = model_to_dict(facebook_profile)

        print(data)

        strategy.session_set('facebook', data)

    # Instagram
    elif backend.name == 'instagram':
        profile = UserProfile.objects.get(user=user)
        print("instagram response: {}".format(response))
        profile.instagram_username = response['user']['username']
        profile.instagram_id = response['user']['id']
        profile.photo_url = response['user']['profile_picture']
        profile.save()

    # LinkedIn
    elif backend.name == 'linkedin':
        print(response)
        linkedin = {
            'l_first_name': response.get('firstName'),
            'l_industry': response.get('industry')
        }
        strategy.session_set('linkedin', linkedin)


