from django import template
register = template.Library()

import json

@register.filter
def get_pokemon_name(value):
    return value.pokemon.name

@register.filter
def get_type(value):
    return type(value)

@register.filter
def get_front_sprite(value):
    str_json = json.loads(value)
    return str_json['front_default']

# @register.filter
# def get_pokemon_sprite(value):
#     pokemon_id = value.pokemon.id
#     pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
#     return PokemonSprites.objects.filter(pokemon.name = value.pokemon.name)
