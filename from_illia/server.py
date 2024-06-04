from flask import Flask
from .game import get_all_pokemons

poks = get_all_pokemons()
pok_t = """<tr>
     <td>{pok.name}</td>
          <td>{pok.weight}</td>
          <td><img src="{pok.picture}" class="img-thumbnail"></td>
        </tr>"""
app = Flask(__name__)
f = open("from_illia/table.html", "r")
template = f.read()
f.close()


@app.route("/")
def hello_world():
    rendered = []
    for pok in poks[:100]:
        rendered.append(pok_t.format(pok=pok))

    return template.format("".join(rendered))
