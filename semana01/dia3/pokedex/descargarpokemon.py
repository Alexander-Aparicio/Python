import requests
import json

BASE_URL= 'http://pokeapi.co/api/v2/pokemon/'

def consultarPokedApi(nombrePokemon):
  url = BASE_URL + nombrePokemon
  response = requests.get(url)

  if response.status_code == 200:
      return json.loads(response.text)
  else:
      return None

if __name__ == '__main__':
  pass