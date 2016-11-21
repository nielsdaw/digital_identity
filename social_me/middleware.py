from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from django.shortcuts import HttpResponse
from social import exceptions as social_exceptions


# TODO Update or delete this middleware - (if no usage)
class TestMiddleware(SocialAuthExceptionMiddleware):

    def process_exception(request, exception):
        if hasattr(social_exceptions, 'AuthCanceled'):
            return HttpResponse("I'm the Pony %s" % exception)
        else:
            raise exception

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response





