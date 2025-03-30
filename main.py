from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "KleberBot está online."

@app.route("/treinamento", methods=["GET", "POST"])
def treinamento():
    if request.method == "POST":
        dados = request.get_json()
        with open("training/kleber-data.json", "w") as f:
            json.dump(dados, f, indent=2)
        return jsonify({"status": "Treinamento atualizado com sucesso."})
    else:
        with open("training/kleber-data.json") as f:
            dados = json.load(f)
        return jsonify(dados)

@app.route("/numeros-bloqueados", methods=["GET", "POST"])
def numeros_bloqueados():
    if request.method == "POST":
        dados = request.get_json()
        with open("config/numeros-bloqueados.json", "w") as f:
            json.dump(dados, f, indent=2)
        return jsonify({"status": "Lista de números bloqueados atualizada."})
    else:
        with open("config/numeros-bloqueados.json") as f:
            dados = json.load(f)
        return jsonify(dados)

if __name__ == "__main__":
    app.run(debug=True)