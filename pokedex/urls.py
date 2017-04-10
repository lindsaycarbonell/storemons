from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.pokedex_list, name='pokedex_list'),
]
