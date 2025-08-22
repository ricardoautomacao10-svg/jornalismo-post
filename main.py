
from flask import Flask, request, jsonify
from utils.coletor import extrair_noticia
from utils.gerador import gerar_html_completo

app = Flask(__name__)

@app.route("/", methods=["GET"])
def gerar_artigo():
    url = request.args.get("url")
    if not url:
        return jsonify({"erro": "Parâmetro 'url' é obrigatório"}), 400
    try:
        titulo, texto, imagem = extrair_noticia(url)
        html = gerar_html_completo(titulo, texto, imagem)
        return html
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
