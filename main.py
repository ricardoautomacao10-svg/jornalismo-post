from flask import Flask, send_file
from utils.coletor import extrair_noticia
from utils.gerador import gerar_conteudo_completo
import os

app = Flask(__name__)

@app.route("/")
def gerar_artigo():
    url = "https://www.ubatuba.sp.gov.br/noticias/estudantesiniciam06ago/"
    print("🔍 Buscando notícias no Google News...")
    print(f"📰 Coletando: {url}")

    titulo, texto, imagem = extrair_noticia(url)

    print("✅ Extração concluída. Gerando conteúdo...")

    gerar_conteudo_completo(titulo, texto, imagem, url)

    print("✅ Texto gerado e disponível.")
    return "Artigo gerado. Acesse /ultima_noticia para visualizar."

@app.route("/ultima_noticia")
def serve_html():
    return send_file("public/ultima_noticia.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
