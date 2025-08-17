# Pokédex Flask

Uma aplicação web simples de **Pokédex** construída com **Flask**, que permite buscar informações de qualquer Pokémon usando a [PokéAPI](https://pokeapi.co/). O projeto exibe dados como tipos, altura, peso, habilidades, stats e até o som do Pokémon.

---

## Funcionalidades

- Busca de Pokémon pelo **nome**.
- Exibição de:
  - Foto do Pokémon
  - Tipos
  - Espécie
  - Altura e Peso
  - Stats (HP, Attack, Defense, etc.) com animação visual
  - Áudio do grito do Pokémon
- Feedback amigável para:
  - Pokémon não encontrado
  - Campos de busca vazios
- Layout moderno, responsivo e interativo.

---

## Tecnologias Utilizadas

- **Python 3**
- **Flask** – framework web
- **Requests** – para consumir a PokéAPI
- **HTML/CSS/JS** – interface do usuário
- **PokéAPI** – base de dados Pokémon

---

## Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/pokedex-flask.git
cd pokedex-flask

---

2. Crie um ambiente virtual (opcional, mas recomendado):
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

---

3. Instale as dependências:
pip install flask requests

---

4. Execute:
python pokedex.py

---

5. Acesse:
http://127.0.0.1:5000/home

---

