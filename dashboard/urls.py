from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.MainProfileView.as_view(), name='main'),
]