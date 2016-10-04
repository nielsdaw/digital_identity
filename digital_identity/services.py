import requests
import json


# --- Instagram services ---

def get_recent_instagram_photos(auth_token):
    """ Call the instagram API to get all photos from user with auth token.
        Return a list with all photo url's
    """
    url = 'https://api.instagram.com/v1/users/self/media/recent/'
    params = {'access_token': auth_token}
    r = requests.get(url, params=params)
    recent_photos = r.json()
    url_of_photos = []
    for item in recent_photos['data']:
        url_of_photos.append(item['images']['standard_resolution']['url'])
    return url_of_photos


def get_fb_photo_url(auth_token, height, width):
    """ Call the facebook API to get users profile picture with specified
        height and width, by using auth token.
        Parameters:
            auth_token - the user auth_token
            height - int value of the height
            width - int value of the width
        Return:
                Return a string of URL to photo
    """
    url = 'https://graph.facebook.com/me/picture?redirect=false'
    params = {'access_token': auth_token, 'height': height, 'width': width}
    r = requests.get(url, params=params)
    photo_url = r.json()
    return photo_url['data']['url']
