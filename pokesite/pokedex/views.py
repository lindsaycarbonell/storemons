# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import *

def index(request):
    all_pokemon = Pokemon.objects.order_by('name')
    context = {
        'all_pokemon': all_pokemon,
    }
    return render(request, 'pokedex/index.html', context)
    # output = ', '.join([p.name for p in all_pokemon])
    # return HttpResponse(output)

def detail(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    species = get_object_or_404(PokemonSpecies, pk=pokemon_id)
    moves = Move.objects.filter(pokemonmove__pokemon=pokemon)
    return render(request, 'pokedex/detail.html', {'pokemon': pokemon, 'species': species, 'moves': moves})
