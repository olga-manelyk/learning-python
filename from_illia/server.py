from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return """
    <a href="http://127.0.0.1:5000/olga">Greet Olga</a>

    <p>Hello, <b>World</b>!</p>"""


@app.route("/olga")
def hello_olga():
    return "<p>Hello, olga!</p>"
