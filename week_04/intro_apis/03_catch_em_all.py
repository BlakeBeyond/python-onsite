'''
Using the PokéAPI https://pokeapi.co/docs/v2.html#pokemon
fetch the name and height of all 151 Pokémon of the main series.

Create a text document that describes each Pokémon using the information
available in the JSON response.
NOTE: only using 'height' is enough, but if you want more, go crazy.

BONUS: Using your script, create a folder and download the main 'front_default'
       sprites for each Pokémon using requests into that folder.
       Name the files appropriately using the name data from your response.

'''
import requests
for num in range(1, 151):
    url = f'https://pokeapi.co/api/v2/pokemon/{num}'
    r = requests.get(url)
    rj = r.json()
    name = rj['forms'][0]['name']
    print(name)
    height = rj['height']
    print(height)