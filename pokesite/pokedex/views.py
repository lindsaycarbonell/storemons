# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import *

def index(request):
    all_pokemon = Pokemon.objects.order_by('id')
    types = PokemonType.objects.all()
    return render(request, 'pokedex/index.html', {'all_pokemon': all_pokemon, 'types': types})

def detail(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    species = get_object_or_404(PokemonSpecies, pk=pokemon_id)
    moves = Move.objects.filter(pokemonmove__pokemon=pokemon)
    return render(request, 'pokedex/detail.html', {'pokemon': pokemon, 'species': species, 'moves': moves})

# def compare(request, pokemon1_id, pokemon2_id):
#     pokemon1 = get_object_or_404(Pokemon, name=pokemon1_id)
#     pokemon2 = get_object_or_404(Pokemon, name=pokemon2_id)
#
#     return render(request, 'pokedex/compare.html', {pokemon1: 'pokemon1', pokemon2: 'pokemon2'})
#
#     return HttpResponseRedirect(reverse('compare', args=(pokemon1.id, pokemon2.id,)))
