import requests
import spotipy
import flickrapi

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
    print(recent_photos)
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
    print("photo url {}".format(photo_url))
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
    photo_url = r.json()
    print("id photo url {}".format(photo_url))
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
    print("cafe & bars: {}".format(result))
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

    # hotfix to get pretty img else insert dunmmy data
    if list_of_bars:
        list_of_bars[0][2] = get_fb_photo_url_by_id(auth_token, list_of_bars[0][3], 100, 100)
    else:
        list_of_bars.append(["You haven't liked any bars or nightclubs", "0", "http://placehold.it/150x150", "0"])

    # hotfix to get pretty img else insert dunmmy data
    if list_of_cafes:
        list_of_cafes[0][2] = get_fb_photo_url_by_id(auth_token, list_of_cafes[0][3], 100, 100)
    else:
        list_of_cafes.append(["You haven't liked any cafes or restaurants", "0", "http://placehold.it/150x150", "0"])

    # return lists in a list
    response = [list_of_cafes, list_of_bars]
    print("list: {}".format(response))
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
    print("likes loc: {}".format(result))
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
    print("tagged p: {}".format(result))
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


# ---- Spotify services ---

def get_spotify_artists(auth_token):
    """
    Get top artists for user in list of list [0] name, [1] img-url.
    :param auth_token:
    :return: list of lists
    """
    sp = spotipy.Spotify(auth=auth_token)
    artists = []
    top_artists = sp.current_user_top_artists(5, 0, 'long_term')
    for item in top_artists['items']:
        artists.append(
            [
                item['name'],
                item['images'][0]['url']
            ]
        )
    return artists

def get_spotify_tracks(auth_token):
    """
    Get top tracks for user in list of list [0] track-name, [1] album-name, [2] img-url.
    :param auth_token:
    :return: list of lists
    """
    sp = spotipy.Spotify(auth=auth_token)
    result = sp.current_user_top_tracks(5, 0, 'long_term')
    top_tracks = []
    for item in result['items']:
        top_tracks.append(
            [
                item['name'],
                item['album']['name'],
                item['album']['images'][0]['url']
            ]
        )
    return top_tracks



# --- flickr services ---


def get_flickr_image_linkedin(string):
    """
    Get an image url for search string, based on LinkedIn search.
    If the word 'at' is found, the string will be sliced after 'at' to the end
    :param string:
    :return: photo url or empty string
    """
    api_key ="547355d7b9210ad86fbbec85af8c0bc7"
    api_secret = "61b624c29e15f2d8"
    search_string = ""

    bad_search_words = {'Student': True,
                        'Working': True,
                        'Searching': True,

                        }
    count = 0

    # check the words
    for word in string.split():
        if 'at' in word:
            search_string = string[(count+4):]
            break
        if word.istitle() and word not in bad_search_words:
            search_string += " {}".format(word)
        count += len(word)
    flickr = flickrapi.FlickrAPI(api_key, api_secret,format='parsed-json')
    extras = 'url_c'
    result = flickr.photos.search(text=search_string, per_page=1, extras=extras)
    try:
        photo_url = result['photos']['photo'][0]['url_c']
        return photo_url
    except KeyError:
        return ""


def get_flickr_image(string):
    """
    Get an image url for search string.
    :param string:
    :return: photo url or empty string
    """
    api_key ="547355d7b9210ad86fbbec85af8c0bc7"
    api_secret = "61b624c29e15f2d8"
    search_string = ""
    flickr = flickrapi.FlickrAPI(api_key, api_secret,format='parsed-json')
    extras = 'url_c'
    result = flickr.photos.search(text=search_string, per_page=1, extras=extras)
    try:
        photo_url = result['photos']['photo'][0]['url_c']
        return photo_url
    except KeyError:
        return ""








