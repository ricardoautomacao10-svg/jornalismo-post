from flask import Flask, request, render_template
from utils.coletor import extrair_noticia
from utils.gerador import gerar_artigo_completo

app = Flask(__name__)

@app.route("/")
def gerar_artigo():
    url = request.args.get("url")
    if not url:
        return "URL não fornecida", 400
    try:
        titulo, texto, imagem = extrair_noticia(url)
        artigo = gerar_artigo_completo(titulo, texto)
        return render_template("artigo.html", titulo=titulo, texto=artigo, imagem=imagem)
    except Exception as e:
        return f"Erro: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
