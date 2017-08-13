from django import template
register = template.Library()
from pokedex.models import *
from django.shortcuts import get_object_or_404

import json

####################
## PYTHON FILTERS ##
####################
@register.filter
def get_python_type(value):
    return type(value)

##########################
## DB RETRIEVAL FILTERS ##
##########################
@register.filter
def get_type1(value):
    type1 = PokemonType.objects.get(pokemon=value,slot=1)
    return type1.type.name

@register.filter
def get_type2(value):
    try:
        type2 = PokemonType.objects.get(pokemon=value, slot=2)
        return type2.type.name
    except PokemonType.DoesNotExist:
        return False

########################
## DEPRICATED FILTERS ##
########################

# @register.filter
# def get_pokemon_name(value):
#     return value.pokemon.name

# @register.filter
# def get_front_sprite(value):
#     str_json = json.loads(value)
#     return str_json['front_default']
