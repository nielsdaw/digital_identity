from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.MainProfileView.as_view(), name='main'),
    url(r'^facebook$', views.FacebookDetailView.as_view(), name='facebook'),
]