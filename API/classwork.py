import requests

# Base API URL
BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon_data(pokemon_name):
    """
    Fetches data from the Pokémon API for the given Pokémon name.
    """
    url = f"{BASE_URL}{pokemon_name.lower()}"  # Convert name to lowercase for API consistency
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"🐉 Pokémon: {data['name'].capitalize()}")
        print(f"🆔 ID: {data['id']}")
        print(f"📏 Height: {data['height']}")
        print(f"⚖️ Weight: {data['weight']}")
        print("🛡 Abilities:")
        for ability in data['abilities']:
            print(f"  - {ability['ability']['name'].capitalize()}")

    else:
        print(f"⚠️ Error: Could not fetch data for {pokemon_name} (Status Code: {response.status_code})")


get_pokemon_data("pikachu")

get_pokemon_data("bulbasaur")

get_pokemon_data("charmander")