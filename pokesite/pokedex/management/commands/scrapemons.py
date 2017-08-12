# https://docs.djangoproject.com/en/1.11/howto/custom-management-commands/
from django.core.management.base import BaseCommand, CommandError
import requests
import json

BASE_URL = 'http://pokeapi.co/api/v2/'

class Command(BaseCommand):


    def query_pokeapi(resource_url, filename):
        url = '{0}{1}'.format(BASE_URL, resource_url)
        response = requests.get(url)

        if response.status_code == 200:
            data = json.loads(response.content)
            for stat in data['stats']:
                for attr, val in stat.iteritems():

                    if attr == 'stat':
                        this_stat_name = stat[attr]['name']
                        this_base_stat = stat['base_stat']
                        if this_stat_name == 'speed':
                            base_speed = this_base_stat
                        elif this_stat_name == 'special-defense':
                            base_spdef = this_base_stat
                        elif this_stat_name == 'special-attack':
                            base_spatk = this_base_stat
                        elif this_stat_name == 'defense':
                            base_def = this_base_stat
                        elif this_stat_name == 'attack':
                            base_atk = this_base_stat
                        elif this_stat_name == 'hp':
                            base_hp = this_base_stat

    query_pokeapi('pokemon/charizard', 'data/charizard.json')

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Charizard!"))
