from flask import Flask, jsonify

from utils import get_news

G1_URL = "https://g1.globo.com/"
GE_URL = "https://ge.globo.com/"


app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


@app.route("/")
def index():
    return (
        r"<h1>Hello! App is running</h1>"
        r"<h2>Allowed routes:</h2>"
        r"<p><a href='http://localhost:5000/noticiais/gerais'>/noticiais/gerais</a></p>"
        r"<p><a href='http://localhost:5000/noticiais/esportes'>/noticiais/esportes</a></p>"
    )


@app.route("/noticiais/gerais")
def get_g1_news():
    return jsonify(get_news(G1_URL))


@app.route("/noticiais/esportes")
def get_ge_news():
    return jsonify(get_news(GE_URL))
