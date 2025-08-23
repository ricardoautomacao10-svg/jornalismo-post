from flask import Flask, request, render_template
from utils.coletor import extrair_noticia
from utils.gerador import gerar_texto_jornalistico
import os

app = Flask(__name__)

@app.route('/')
def gerar_artigo():
    url = request.args.get('url')
    if not url:
        return {"erro": "Parâmetro 'url' é obrigatório"}, 400

    try:
        titulo, texto_original, imagem_url = extrair_noticia(url)
        artigo = gerar_texto_jornalistico(titulo, texto_original)
        return render_template("artigo.html", titulo=titulo, imagem=imagem_url, texto=artigo)
    except Exception as e:
        return {"erro": f"Erro ao gerar artigo: {str(e)}"}, 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
