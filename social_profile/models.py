from django.db import models
from django.contrib.auth.models import User

# TODO restart all models in database

class UserProfile(models.Model):
    # TODO update this model - delete it maybe?
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook_username = models.TextField(default="")
    facebook_id = models.TextField(default="")
    photo_url = models.TextField(default="")
    instagram_id = models.TextField(default="")
    instagram_username = models.TextField(default="")


    def __str__(self):
        return "fb_username: {}'" \
               "facebook_id: {}"\
               "inst_id: {} "\
               "inst_username: {}".format(
            self.facebook_username,
            self.facebook_id,
            self.instagram_id,
            self.instagram_username
        )


class FacebookManager(models.Manager):
    """Manager for the FacebookProfile Model"""

    def create_facebook_profile(
            self,
            facebook_id,
            first_name,
            last_name,
            facebook_email,
            gender,
            profile_picture_url,
            friends_count,
            link,
            age_range,
            last_updated,
            auth_token
    ):
        facebook_profile = self.create(
            facebook_id=facebook_id,
            first_name=first_name,
            last_name=last_name,
            facebook_email=facebook_email,
            gender=gender,
            profile_picture_url=profile_picture_url,
            friends_count=friends_count,
            link=link,
            age_range=age_range,
            last_updated=last_updated,
            auth_token=auth_token
        )
        return facebook_profile


class FacebookProfile(models.Model):
    """ FacebookProfile Model, used to store data from the Facebook API """

    facebook_id = models.IntegerField(default=0)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    facebook_email = models.EmailField(default="")
    gender = models.CharField(max_length=20)
    profile_picture_url = models.TextField(default="")
    friends_count = models.IntegerField(default=0)  # friends['summary']['total_count']
    link = models.TextField(default="")
    age_range = models.IntegerField(default=0)
    last_updated = models.DateTimeField(default="")
    auth_token = models.TextField(default="")

    objects = FacebookManager()


class InstagramManager(models.Manager):
    """Manager for the InstagramProfil Model"""

    def create_instagram_profile(
            self,
            instagram_id,
            profile_picture_url,
            bio,
            website,
            username,
            full_name,
            access_token,
            number_of_followers,
            number_of_pictures,
            number_of_following
    ):
        instagram_profile = self.create(
            instagram_id=instagram_id,
            profile_picture_url=profile_picture_url,
            bio=bio,
            website=website,
            username=username,
            full_name=full_name,
            access_token=access_token,
            number_of_followers=number_of_followers,
            number_of_pictures=number_of_pictures,
            number_of_following=number_of_following
        )
        return instagram_profile


class InstagramProfile(models.Model):
    """ InstagramProfile Model, used to store data from the Instagram API """

    instagram_id = models.IntegerField(default=0)
    profile_picture_url = models.TextField(default="")
    bio = models.TextField(default="")
    website = models.CharField(default="", max_length=100)
    username = models.CharField(default="", max_length=255)
    full_name = models.CharField(default="", max_length=255)
    access_token = models.TextField(default="")
    number_of_followers = models.IntegerField(default=0)
    number_of_pictures = models.IntegerField(default=0)
    number_of_following = models.IntegerField(default=0)

    objects = InstagramManager()


class TwitterProfile(models.Model):
    # TODO create this model - Twitter
    pass


#class LinkedInProfile(models.Model):
 #   pass


class SoundCloudProfile(models.Model):
    # TODO create this model - SoundCLoud
    pass


class SpotifyProfile(models.Model):
    # TODO create this model - Spotify
    pass


class GoogleProfile(models.Model):
    # TODO create this model - GoogleProfile
    pass


