"""
WSGI config for digital_identity project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os


from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "digital_identity.settings")

application = Cling(get_wsgi_application())
application = DjangoWhiteNoise(application)


# -- original setting local
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "digital_identity.settings")
#
# application = get_wsgi_application()
