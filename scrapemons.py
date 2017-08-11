import requests
import json

BASE_URL = 'http://pokeapi.co'

def query_pokeapi(resource_url):
    url = '{0}{1}'.format(BASE_URL, resource_url)
    response = requests.get(url)

    if response.status_code == 200:
        # return json.loads(response.text)
        return response.content
    return None

charizard = query_pokeapi('/api/v2/pokemon-species/charizard')

# print charizard['evolution_chain']['url']

with open('charizard.json', 'w') as outf:
    outf.write(charizard)
