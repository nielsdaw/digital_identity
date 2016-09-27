import requests


# --- Instagram services ---

def get_recent_photos(auth_token):
    url = 'https://api.instagram.com/v1/users/self/media/recent/'
    params = {'access_token': auth_token}
    r = requests.get(url, params=params)
    photos = r.json()
    print("instagram photos json: {}".format(photos))