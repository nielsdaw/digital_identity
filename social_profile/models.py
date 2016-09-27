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


class FacebookManager(models.Manager):
    def create_facebook_profile(
            self,
            fb_id,
            first_name,
            last_name,
            fb_email,
            gender,
            profile_picture_url,
            friends_count,
            link,
            age_range,
            last_updated
    ):
        facebook_profile = self.create(
            fb_id=fb_id,
            first_name=first_name,
            last_name=last_name,
            fb_email=fb_email,
            gender=gender,
            profile_picture_url=profile_picture_url,
            friends_count=friends_count,
            link=link,
            age_range=age_range,
            last_updated=last_updated
        )
        return facebook_profile


class FacebookProfile(models.Model):
    fb_id = models.IntegerField(default=0)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    fb_email = models.EmailField()
    gender = models.CharField(max_length=20)
    profile_picture_url = models.TextField()
    friends_count = models.IntegerField(default=0)  # friends['summary']['total_count']
    link = models.TextField()
    age_range = models.IntegerField(default=0)
    last_updated = models.DateTimeField()

    objects = FacebookManager()


class InstagramProfile(models.Model):
    pass


class TwitterProfile(models.Model):
    pass


#class LinkedInProfile(models.Model):
 #   pass


class SoundCloudProfile(models.Model):
    pass


class SpotifyProfile(models.Model):
    pass


class UberProfile(models.Model):
    pass


class GoogleProfile(models.Model):
    pass


