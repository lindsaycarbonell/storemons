from django.shortcuts import render

def pokedex_list(request):
    return render(request, 'pokedex/pokedex_list.html', {})
