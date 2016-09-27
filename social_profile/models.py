from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook_username = models.TextField(default="")
    facebook_id = models.TextField(default="")
    photo_url = models.TextField(default="")
    instagram_id = models.TextField(default="")
    instagram_username = models.TextField(default="")


    def __str__(self):
        return "fb_username: {}'" \
               "fb_id: {}"\
               "inst_id: {} "\
               "inst_username: {}".format(
            self.facebook_username,
            self.facebook_id,
            self.instagram_id,
            self.instagram_username
        )


class FacebookProfile(models.Model):
    pass


class InstagramProfile(models.Model):
    pass


class TwitterProfile(models.Model):
    pass


class LinkedInProfile(models.Model):
    pass


class SoundCloudProfile(models.Model):
    pass


class SpotifyProfile(models.Model):
    pass


class UberProfile(models.Model):
    pass


class GoogleProfile(models.Model):
    pass


