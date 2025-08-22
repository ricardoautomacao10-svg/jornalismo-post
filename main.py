from flask import Flask, request, render_template
from utils.coletor import extrair_noticia
from utils.gerador import gerar_texto_jornalistico

app = Flask(__name__)

@app.route("/")
def gerar_artigo():
    url = request.args.get("url")
    if not url:
        return {"erro": "Parâmetro 'url' é obrigatório"}, 400

    titulo, texto_original, imagem = extrair_noticia(url)
    if not texto_original:
        return {"erro": "Erro ao extrair notícia"}, 500

    texto_gerado = gerar_texto_jornalistico(titulo, texto_original)
    if not texto_gerado:
        return {"erro": "Erro ao gerar texto com IA"}, 500

    return render_template("resultado.html", titulo=titulo, texto=texto_gerado, imagem=imagem)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
