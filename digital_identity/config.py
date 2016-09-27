

# -- Social Auth Settings --

# Redirects

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login-error/'


# Add to pipeline

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.mail.mail_validation',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'social_profile.pipeline.update_profile',
)

# pipeline session fields

FIELDS_STORED_IN_SESSION = ['linkedin', ]


# Profile model

AUTH_PROFILE_MODULE = 'social_profile.models.UserProfile'


# -- backend settings ---


# Instagram auth

SOCIAL_AUTH_INSTAGRAM_KEY = '23a136f34a1140c7acdb500b934cd885'

SOCIAL_AUTH_INSTAGRAM_SECRET = 'aca530c8df194fa680dfca86aaa26363'

SOCIAL_AUTH_INSTAGRAM_AUTH_EXTRA_ARGUMENTS = {
    'scope': 'likes comments relationships'
}


# facebook auth

SOCIAL_AUTH_FACEBOOK_KEY = '1145374812173983'

SOCIAL_AUTH_FACEBOOK_SECRET = 'aa7ef2b78c17b984b43ff4b55f1d2bd9'

SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'public_profile',
    'email',
    'user_friends',
]

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'fields': 'id,'
            'name,'
            'first_name,'
            'last_name,'
            'picture,'
            'email,'
            'age_range,'
            'link,'
            'gender,'
            'locale,'
            'timezone,'
            'updated_time,'
            'friends'

}

# -- Public available fields --
# 'id,'
# 'name,'
# 'first_name,'
# 'last_name,'
# 'link,'
# 'gender,'
# 'locale,'
# 'picture,'
# 'email,'
# 'age_range,'
# 'timezone,'
# 'updated,'
# 'birthday,'
# 'about,'
# 'data,'
# 'paging,'
# 'summary'
# 'friends' ['data'] or ['summary']


# LinkedIn settings

SOCIAL_AUTH_LINKEDIN_KEY = '77mgcls2owj2is'

SOCIAL_AUTH_LINKEDIN_SECRET = 'Z0yza5BLiAfq7xV6'

SOCIAL_AUTH_LINKEDIN_SCOPE = ['r_basicprofile',]

SOCIAL_AUTH_LINKEDIN_FIELD_SELECTORS = ['email-address', 'headline', 'industry']

SOCIAL_AUTH_LINKEDIN_EXTRA_DATA = [('id', 'id'),
                                   ('firstName', 'first_name'),
                                   ('lastName', 'last_name'),
                                   ('emailAddress', 'email_address'),
                                   ('headline', 'headline'),
                                   ('industry', 'industry')]

