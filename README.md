# My Pokédex

Uma Pokédex web interativa feita em **Flask** que permite buscar e visualizar informações detalhadas de Pokémon, incluindo imagem, tipos, estatísticas, habilidades e até o som do "cry" de alguns Pokémon.

---

## Funcionalidades

- Buscar Pokémon por nome.
- Exibir imagem, tipo, altura, peso e espécie.
- Mostrar habilidades e estatísticas detalhadas.
- Tocar o "cry" do Pokémon (quando disponível).
- Interface responsiva e estilizada com CSS3.

---

## Tecnologias

- Python 3.11
- Flask
- Jinja2 (templates)
- HTML5 / CSS3
- Git & GitHub

---

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/wallingson12/My-pokedex.git
cd My-pokedex

python -m venv .venv
source .venv/bin/activate  # Linux / macOS
.venv\Scripts\activate     # Windows

pip install -r requirements.txt

python Pokedex.py

http://127.0.0.1:5000

My-pokedex/
├── models/             # Classes e dados dos Pokémon
├── static/             # CSS e imagens
│   ├── imagens/        # Fundo e imagens de Pokémon
│   └── style.css       # Estilos da página
├── templates/          # HTML templates
│   └── pokedex.html
├── Pokedex.py          # Aplicação Flask
├── requirements.txt    # Dependências do projeto
└── README.md
