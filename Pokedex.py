from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def obter_tipo_pokemon(nome_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        if 'types' in pokemon_data:
            types = [entry['type']['name'] for entry in pokemon_data['types']]
            return types
    return None

@app.route("/")
def pokedex():
    return render_template('index.html', pokemon=None, message=None)

@app.route("/buscar", methods=["POST"])
def buscar():
    try:
        pokemon_name = request.form["nome"].lower()

        # Obtém o tipo do Pokémon
        tipos_pokemon = obter_tipo_pokemon(pokemon_name)

        # Monta os dados do Pokémon
        pokemon = {
            'nome': pokemon_name,
            'tipo': tipos_pokemon[0] if tipos_pokemon else None,  # Apenas o primeiro tipo por simplicidade
            'foto': None
        }

        # Obtém a imagem do Pokémon
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
        if response.status_code == 200:
            pokemon_data = response.json()
            if 'sprites' in pokemon_data and 'front_default' in pokemon_data['sprites']:
                pokemon['foto'] = pokemon_data['sprites']['front_default']

        return render_template('pokedex.html', pokemon=pokemon, message=None)

    except Exception as e:
        return render_template('pokedex.html', pokemon=None, message=f"Erro ao buscar o Pokémon: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
