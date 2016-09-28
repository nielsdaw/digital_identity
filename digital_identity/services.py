import requests
import json


# --- Instagram services ---

def get_recent_photos(auth_token):
    """ Call the instagram API to get all photos from user with auth token.
        Return a list with all photo url,s
    """
    url = 'https://api.instagram.com/v1/users/self/media/recent/'
    params = {'access_token': auth_token}
    r = requests.get(url, params=params)
    recent_photos = r.json()
    url_of_photos = []
    for item in recent_photos['data']:
        url_of_photos.append(item['images']['standard_resolution']['url'])
    return url_of_photos

