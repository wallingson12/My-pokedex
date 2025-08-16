from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder="templates")

def obter_dados_pokemon(nome_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

@app.route("/")
def pokedex():
    return render_template('pokedex.html', pokemon=None, message=None)

@app.route("/buscar", methods=["POST"])
def buscar():
    try:
        pokemon_name = request.form["nome"].lower()
        pokemon_data = obter_dados_pokemon(pokemon_name)

        if not pokemon_data:
            return render_template('pokedex.html', pokemon=None, message="Pokémon não encontrado!")

        # Monta dados do Pokémon
        pokemon_id = pokemon_data['id']
        cry_url = f"https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/{pokemon_id}.ogg"

        pokemon = {
            'nome': pokemon_name,
            'tipo': [entry['type']['name'] for entry in pokemon_data['types']],
            'foto': pokemon_data.get('sprites', {}).get('other', {}).get('dream_world', {}).get('front_default'),
            'species': pokemon_data['species']['name'] if 'species' in pokemon_data else None,
            'height': pokemon_data['height'],
            'weight': pokemon_data['weight'],
            'stats': {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']},
            'cry': cry_url
        }

        return render_template('pokedex.html', pokemon=pokemon, message=None)

    except Exception as e:
        return render_template('pokedex.html', pokemon=None, message=f"Erro ao buscar o Pokémon: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
