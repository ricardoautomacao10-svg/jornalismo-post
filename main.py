from flask import Flask, request, jsonify
from utils.coletor import extrair_noticia
from utils.gerador import gerar_texto

app = Flask(__name__)

@app.route("/", methods=["GET"])
def gerar_artigo():
    url = request.args.get("url")
    if not url:
        return jsonify({"erro": "URL não fornecida"}), 400

    try:
        titulo, conteudo, imagem = extrair_noticia(url)
        texto_final = gerar_texto(titulo, conteudo)
        return jsonify({"titulo": titulo, "texto": texto_final, "imagem": imagem})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
