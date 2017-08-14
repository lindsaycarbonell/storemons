from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pokemon_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^compare/(?P<pokemon2>[0-9]+)(?P<pokemon1>[0-9]+)$', views.compare, name='compare'),

]
