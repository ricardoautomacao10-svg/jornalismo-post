from flask import Flask, request, render_template
from utils.coletor import extrair_noticia
from utils.gerador import gerar_texto_completo

app = Flask(__name__)

@app.route('/')
def gerar_artigo():
    url = request.args.get('url')
    if not url:
        return "Erro: parâmetro 'url' ausente", 400
    try:
        titulo, texto, imagem = extrair_noticia(url)
        artigo_html = render_template("artigo.html", titulo=titulo, texto=texto, imagem=imagem)
        with open("static/artigo.html", "w", encoding="utf-8") as f:
            f.write(artigo_html)
        return artigo_html
    except Exception as e:
        return f"Erro ao gerar artigo: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
