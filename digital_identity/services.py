import requests
import spotipy
from instagram.client import InstagramAPI

import json


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


    # access_token = "YOUR_ACCESS_TOKEN"
    # client_secret = "YOUR_CLIENT_SECRET"
    # api = InstagramAPI(access_token=access_token, client_secret=client_secret)
    # recent_media, next_ = api.user_recent_media(user_id="userid", count=10)
    # for media in recent_media:
    #    print media.caption.text



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






