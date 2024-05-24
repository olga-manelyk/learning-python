import os
import json
from time import sleep
from webbrowser import open_new_tab
from dataclasses import dataclass
import requests

url = "https://pokeapi.co/api/v2/pokemon"
urls_filename = "pokemon_urls.json"
full_info_filename = "pokemon_full_info.json"


@dataclass
class Pokemon:
    id: int
    name: str
    weight: int
    picture: str

    def show_picture(self):
        open_new_tab(self.picture)


def _get_pokemon_urls():
    if os.path.exists(urls_filename):
        print("Loading all pokemon urls from file")
        with open(urls_filename, "r") as f:
            return json.loads(f.read())
    print("Fetching all pokemon urls")
    pokemon_urls = []
    next_url = url
    while next_url:
        print(f"Fetching {next_url}")
        response = requests.get(next_url)
        pokemon_urls.extend(response.json()["results"])
        next_url = response.json()["next"]
        sleep(1)
    with open(urls_filename, "w") as f:
        f.write(json.dumps(pokemon_urls, sort_keys=True, indent=4))
    return pokemon_urls


def get_all_pokemons():
    if os.path.exists(full_info_filename):
        print("Loading all pokemon info from file")
        with open(full_info_filename, "r") as f:
            return [Pokemon(**pokemon) for pokemon in json.loads(f.read())]
    pokemon_urls = _get_pokemon_urls()
    print("Fetching all pokemon info")
    pokemons_info = []
    for pokemon_url in pokemon_urls:
        print(f"Fetching {pokemon_url['url']}")
        response = requests.get(pokemon_url["url"])
        pokemon = {
            "id": response.json()["id"],
            "name": response.json()["name"],
            "weight": response.json()["weight"],
            "picture": response.json()["sprites"]["front_default"],
        }
        pokemons_info.append(pokemon)
    with open(full_info_filename, "w") as f:
        f.write(json.dumps(pokemons_info, sort_keys=True, indent=4))
    return [Pokemon(**pokemon) for pokemon in pokemons_info]


poks = get_all_pokemons()
result = {}

for pok in poks:
    name_length = len(pok.name)

    if name_length in result:
        result[name_length] = result[name_length] + 1
    else:
        result[name_length] = 1
print(result)
