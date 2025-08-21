from flask import Flask, request, render_template_string
from utils.coletor import extrair_noticia
from utils.gerador import gerar_texto_completo

app = Flask(__name__)

@app.route("/", methods=["GET"])
def gerar_artigo():
    url = request.args.get("url")
    if not url:
        return "Parâmetro 'url' é obrigatório", 400

    try:
        titulo, texto_base, imagem = extrair_noticia(url)
        artigo_html = gerar_texto_completo(titulo, texto_base, imagem)
        return render_template_string(artigo_html)
    except Exception as e:
        return f"Erro: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
