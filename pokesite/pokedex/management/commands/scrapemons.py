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
            with open(filename, 'w') as outf:
                outf.write(response.content)

    query_pokeapi('pokemon-species/charizard', 'data/charizard.json')

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Charizard!"))

    # print "Charizard was written to the root folder"
