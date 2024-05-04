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


from pprint import pprint

p = get_all_pokemons()

# 1.1.1
sum_of_weight = 0
# 1.1.2
for pok in p:
    sum_of_weight = sum_of_weight + pok.weight
print("Sum of weights of all Pokémon:", sum_of_weight)
# 1.2.1
mean_weight = sum_of_weight / len(p)
print(mean_weight)
# 2.1
fat_pokemons = []
for pok in p:
    # 2.3
    if pok.weight > mean_weight:
        fat_pokemons.append(pok)
pprint(fat_pokemons)
