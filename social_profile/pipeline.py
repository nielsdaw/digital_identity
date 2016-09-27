from social_profile.models import UserProfile


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
        linkedin = {
            'l_first_name': response.get('firstName'),
            'l_industry': response.get('industry')
        }
        strategy.session_set('linkedin', linkedin)
    #     profile = LinkedInProfile.objects.get(user=user)
    #     print("linkedin response: {}".format(response))
    #     profile.first_name = response.get('firstName')
    #     profile.last_name = response.get('lastName')
    #     profile.industry = response.get('industry')
    #     print(profile.industry)
    #     return profile


    #profile.save()

