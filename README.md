# Storemons
Using the Pokémon API to store my 'mons


http://pykemon.readthedocs.io/en/latest/usage.html

https://tutorial.djangogirls.org/en/django_start_project/


## Fields
- TABLE: my_pokemon
  - dex_num
  - species
  - nickname
  - original_game
  - species
  - type1
  - type2
  - ability
  - nature
- TABLE: national_dex
  - dex_num
  - species
  - base_hp
  - base_atk
  - base_def
  - base_spdef
  - base_speed
- TABLE: Abilities
- TABLE: Moves
- TABLE: Natures


## Future Features
- There should be an "evolve" option that allows you to select a pre-evolution of a Pokémon in your collection and "evolve" it. This should allow you to alter its moveset and other stats upon evolution.
- There should be an option to "release" a Pokémon, which will completely remove it from the database.
- There should be an option to "transfer" a Pokémon to a different game. (MAYBE THIS SHOULD JUST BE AN EDIT OPTION)
- A section where I can keep track of the mega evolution stones I have.

## Notes for me
http://127.0.0.1:8000/admin/ go here to add Pokemon

## Process
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
