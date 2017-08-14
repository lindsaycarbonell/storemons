# Storemons
This application is for storing and performing various analyses of all Pokémon as of Pokémon Sun and Moon (Generation VII). 

## Features
- Displays all Pokémon at /pokedex
<img src='home1.jpg' />
<img src='home2.jpg' />
- Shows name and sprite on inner page at /pokedex/[dex_num]
<img src='inner.jpg' />

## Developing Features
### Compare Pokémon page


### Other
- Set of models for storing personal Pokémon attributes, including model methods for "evolve", "release", "transfer"
- A section to keep track of obtained mega evolution stones (basically equivalent to owning a -Mega Pokémon)
- Set of models for storing personal Pokémon attributes

## Libraries and Outside Code
- [PokéAPI](https://github.com/PokeAPI/pokeapi): all base models and data are from the PokéAPI repository, without which there would be far less data I would be willing to put into this application myself.
- Bootstrap 4

## Notes for the developer
1. Create a virtual environment. (http://docs.python-guide.org/en/latest/dev/virtualenvs/)
  `virtualenv env`
2. Install Django. Make sure you have Python 3 by running `python3 --version`
  `pip install Django`
3. Create project
  `django-admin startproject pokesite`
4. Create app
  `python manage.py startapp pokedex`

## Helpful links
https://www.twilio.com/blog/2014/11/build-your-own-pokedex-with-django-mms-and-pokeapi.html
http://pykemon.readthedocs.io/en/latest/usage.html
https://tutorial.djangogirls.org/en/django_start_project/
