import random

from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)

CORS(app)


@app.route("/gerar", methods=["POST"])
def gerar():

    dados = request.json

    tamanho = int(dados["tamanho"])

    usar_letras = dados["letras"]
    usar_numeros = dados["numeros"]
    usar_simbolos = dados["simbolos"]

    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    simbolos = "!@#$%&*;:()-_=+[]{}"

    caracteres = ""

    if usar_letras:
        caracteres += letras

    if usar_numeros:
        caracteres += numeros

    if usar_simbolos:
        caracteres += simbolos

    if caracteres == "":
        return jsonify({
            "erro": "Escolha pelo menos uma opção."
        }), 400

    senha = ""

    for i in range(tamanho):
        senha += random.choice(caracteres)

    print("\nSua senha é:")
    print(senha)

    return jsonify({
        "senha": senha
    })


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
