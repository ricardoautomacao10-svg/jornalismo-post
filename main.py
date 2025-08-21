
from flask import Flask, request, jsonify, send_file
from utils.coletor import extrair_noticia
from utils.gerador import gerar_artigo_textsynth
from utils.salvador import salvar_html

app = Flask(__name__)

@app.route("/", methods=["GET"])
def gerar_artigo():
    url = request.args.get("url")
    if not url:
        return jsonify({"erro": "URL da notícia não fornecida"}), 400

    try:
        titulo, texto_original, imagem = extrair_noticia(url)
        texto_final = gerar_artigo_textsynth(titulo, texto_original)
        caminho = salvar_html(titulo, texto_final, imagem)
        return send_file(caminho, mimetype="text/html")
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
