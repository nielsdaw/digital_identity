import requests
import spotipy


# -- General services --

def get_social_medias(request):
    """
    Takes a request and return a dict of social_medias
    :param request:
    :return: a dict of social media(s)
    """
    social_medias = request.session['social_media']
    return social_medias


def check_for_social_media(request, social_media_name):
    """
    Check if the social_media_name is in the current session of the request
    :param request:
    :param social_media_name:
    :return: a dict with the social media or False
    """
    if social_media_name in request.session['social_media']:
        social_media = request.session['social_media'][social_media_name]
        print("what is in session: {}".format(social_media))
        return social_media

    if social_media_name in request.session['social_media']:
        social_media = request.session['social_media'][social_media_name]
        print("what is in session: {}".format(social_media))
        return social_media

    if social_media_name in request.session['social_media']:
        social_media = request.session['social_media'][social_media_name]
        print("what is in session: {}".format(social_media))
        return social_media

    if social_media_name in request.session['social_media']:
        social_media = request.session['social_media'][social_media_name]
        print("what is in session: {}".format(social_media))
        return social_media

    return False


# --- Instagram services ---

def get_recent_instagram_photos(auth_token):
    """
    Call the instagram API to get all photos from user with auth token.
    :param auth_token:
    :return: Return a list with all photo url's
    """
    url = 'https://api.instagram.com/v1/users/self/media/recent/'
    params = {'access_token': auth_token}
    r = requests.get(url, params=params)
    recent_photos = r.json()
    print(recent_photos)
    url_of_photos = []
    for item in recent_photos['data']:
        url_of_photos.append(item['images']['standard_resolution']['url'])
    return url_of_photos


def get_recent_instagram_likes(auth_token):
    """
    Call the instagram API to get all recent likes from user with auth token.
    :param auth_token:
    :return: Return a list with all liked images url's
    """
    url = 'https://api.instagram.com/v1/users/self/media/liked?'
    params = {'access_token': auth_token, 'count': 100}
    r = requests.get(url, params=params)
    print('url: {}'.format(r.url))
    recent_likes = r.json()

    print("recent likes: {}".format(recent_likes))


def get_media_locations(auth_token):
    """
    Get a list of lists with latitude[0], longitude[1], name[2], from instagram photos.
    :param auth_token:
    :return: list of lists
    """
    url = 'https://api.instagram.com/v1/users/self/media/recent/'
    params = {'access_token': auth_token}
    r = requests.get(url, params=params)
    recent_photos = r.json()
    list_of_locations = []
    for item in recent_photos['data']:
        if item['location']:
            list_of_locations.append(
                [item['location']['latitude'],
                 item['location']['longitude'],
                 "<b>{}</b>".format(item['location']['name'])]
            )
    return list_of_locations


# --- Facebook services ---

def get_fb_photo_url(auth_token, height, width):
    """
    Call the facebook API to get users profile picture with specified
    height and width, by using auth token.
    :param auth_token: users authentication token
    :param height: the requested height
    :param width: the requested width
    :return: Return a string of URL to photo
    """
    url = 'https://graph.facebook.com/me/picture?redirect=false'
    params = {'access_token': auth_token, 'height': height, 'width': width}
    r = requests.get(url, params=params)
    photo_url = r.json()
    return photo_url['data']['url']


def get_fb_photo_url_by_id(auth_token, user_id, height, width):
    """
    Call the facebook API to get users profile picture with specified
    height and width, by using auth token.
    :param auth_token: users authentication token
    :param user_id of the user/event/page
    :param height: the requested height
    :param width: the requested width
    :return: Return a string of URL to photo
    """
    url = 'https://graph.facebook.com/' + user_id + '/picture?redirect=false'
    params = {'access_token': auth_token, 'height': height, 'width': width}
    r = requests.get(url, params=params)
    print(r)
    photo_url = r.json()
    return photo_url['data']['url']


def get_cafes_and_bars(auth_token):
    """
    Get a list of cafes and bars/night clubs from facebook Likes
    :param auth_token:
    :return: a list with two lists [0] cafes, [1] bars/night clubs
    """
    url = 'https://graph.facebook.com/me/?fields=likes{category,category_list,name,picture}'
    params = {'access_token': auth_token}
    r = requests.get(url, params=params)
    result = r.json()
    first_loop = True
    if_condition = None
    list_of_cafes = []
    list_of_bars = []
    check_list_of_cafes = {'Breakfast & Brunch Restaurant': True,
                     'Restaurant/Cafe': True,
                     'Cafe': True,
                     'Coffee Shop': True,
                     'Restaurant': True
                     }

    check_list_of_bars = {'Dance & Night Club': True,
                    'Bar': True,
                    'Club': True,
                    'Party Entertainment Venue': True,
                    'Performance & Sports Venue': True,
                    'Live Music Venue': True
                    }

    # loop through the json result and call the next request if exist
    # catch KeyError, if 'next' key doesn't exist, since there are no more likes
    while True:
        try:
            if first_loop:
                if_condition = result['likes']['data']
            else:
                if_condition = result['data']

            # loop through content
            for item in if_condition:
                # check for cafes in category
                if item['category'] in check_list_of_cafes:
                    list_of_cafes.append(
                        [
                            item['name'],
                            item['category'],
                            item['picture']['data']['url'],
                            item['id']
                        ]
                    )
                    continue
                # check for bars in category
                elif item['category'] in check_list_of_bars:
                    list_of_bars.append(
                        [
                            item['name'],
                            item['category'],
                            item['picture']['data']['url'],
                            item['id']
                        ]
                    )
                    continue

                # loop through category_list to check for bars and cafes
                elif 'category_list' in item:
                    for category in item['category_list']:
                        if category['name'] in check_list_of_cafes:
                            list_of_cafes.append(
                                [
                                    item['name'],
                                    category['name'],
                                    item['picture']['data']['url'],
                                    item['id']
                                ]
                            )
                            break

                        elif category['name'] in check_list_of_bars:
                            list_of_bars.append(
                                [
                                    item['name'],
                                    category['name'],
                                    item['picture']['data']['url'],
                                    item['id']
                                ]
                            )
                            break

            # Attempt to make a request to the next page of data, if it exists.
            if first_loop:
                result = requests.get(result['likes']['paging']['next']).json()
                first_loop = False

            # after first request, the response json pattern changes
            else:
                result = requests.get(result['paging']['next']).json()

        except KeyError:
            break

    # return lists in a list
    response = [list_of_cafes, list_of_bars]
    return response


def get_likes_locations(auth_token):
    """
    Get a list of lists with latitude[0], longitude[1], name[2], based from facebook likes.
    :param auth_token:
    :return: list of lists
    """
    url = 'https://graph.facebook.com/me/?fields=likes{category,category_list,name,location}'
    params = {'access_token': auth_token}
    r = requests.get(url, params=params)
    result = r.json()
    list_of_locations = []
    first_loop = True
    if_condition = None

    # loop through the json result and call the next request if exist
    # catch KeyError, if 'next' key doesn't exist, since there are no more likes
    while True:
        try:
            if first_loop:
                if_condition = result['likes']['data']
            else:
                if_condition = result['data']

            for item in if_condition:

                # check for location
                if 'location' in item:

                    # check for latitude (implicitly altitude will be there)
                    if 'latitude' in item['location']:
                        list_of_locations.append(
                            [
                                item['location']['latitude'],
                                item['location']['longitude'],

                                ('<b>{}</b><br><br>{}'.format(item['name'], item['location']['street']) if
                                    'street' in item['location'] else
                                    "<b>{}</b><br><br>".format(item['name']))
                            ]
                        )
            # Attempt to make a request to the next page of data, if it exists.
            if first_loop:
                result = requests.get(result['likes']['paging']['next']).json()
                first_loop = False

            # after first request, the response json pattern changes
            else:
                result = requests.get(result['paging']['next']).json()
        except KeyError:
            break
    return list_of_locations


def get_tagged_places(auth_token):
    """
    Takes auth_token to get all locations of tagged places.
    Creates a list of lists with latitude[0], longitude[1], name[2], from facebook
    :param auth_token:
    :return: list of lists
    """
    url = 'https://graph.facebook.com/me/tagged_places'
    params = {'access_token': auth_token}
    r = requests.get(url, params=params)
    result = r.json()
    list_of_locations = []
    list_of_names = {}
    for item in result['data']:
        if item['place']['location'] and item['place']['name'] not in list_of_names:
            list_of_locations.append(
                [item['place']['location']['latitude'],
                 item['place']['location']['longitude'],
                 "<b>{}</b>".format(item['place']['name'])]
            )
            # make sure there are dublicates
            list_of_names[item['place']['name']] = True

    return list_of_locations




def get_participated_events(auth_token):
    url = 'https://graph.facebook.com/me/?fields=events'
    # url = 'https://graph.facebook.com/me/?fields=events{name,place}'
    params = {'access_token': auth_token}
    r = requests.get(url, params=params)
    result = r.json()
    print(result)




# ---- Spotify services ---

def get_spotify_artists(auth_token):
    """
    :param auth_token:
    :return: top artists of user
    """
    sp = spotipy.Spotify(auth=auth_token)
    top_artists = sp.current_user_top_artists(5, 0, 'long_term')
    return top_artists

def get_spotify_tracks(auth_token):
    """
    :param auth_token:
    :return: top_tracks of user
    """
    sp = spotipy.Spotify(auth=auth_token)
    top_tracks = sp.current_user_top_tracks(5, 0, 'long_term')
    return top_tracks






