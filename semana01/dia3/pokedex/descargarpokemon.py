import requests
import json
import webbrowser
from PIL import Image


BASE_URL= 'http://pokeapi.co/api/v2/pokemon/'

def consultarPokedApi(nombrePokemon):
  url = BASE_URL + nombrePokemon
  response = requests.get(url)

  if response.status_code == 200:
      return json.loads(response.text)
  else:
      return None

if __name__ == '__main__':
  buscar = input('ingrese el pokemon a buscar: ')
  pokemon = consultarPokedApi(buscar)
  if pokemon == None:
    print('No existe Pokemon con ese nombre')
  else:
    # print(pokemon)
    sprites = pokemon['sprites']
    print(sprites['front_default'])
    f = open(buscar + '.jpg','wb')
    # wb: es para indicar que puede escribir coódigo binario
    response = requests.get(sprites['front_default'])
    f.write(response.content)
    f.close()
    print("se descarga la imagen del pokemon")
    webbrowser.open(sprites['front_default'])
    im = Image.open(buscar + '.jpg')
    im.show()
