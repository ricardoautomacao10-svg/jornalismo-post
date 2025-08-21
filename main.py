# app.py
from flask import Flask, send_file, jsonify
from utils.coletor import extrair_noticia
from utils.gerador import gerar_conteudo_completo
import os

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"status": "online"})

@app.route("/noticia")
def noticia():
    if os.path.exists("output.html"):
        return send_file("output.html", mimetype="text/html")
    return "Nenhum conteúdo disponível", 404

@app.route("/executar")
def executar():
    url = "https://www.ubatuba.sp.gov.br/noticias/estudantesiniciam06ago/"  # Pode ser dinâmico depois
    print("🔍 Buscando notícias no Google News...")
    print(f"📰 Coletando: {url}")

    texto = extrair_noticia(url)
    if not texto:
        print("❌ Falha ao extrair texto.")
        return "Erro na extração", 500

    print("✅ Extração concluída. Gerando conteúdo...")
    artigo = gerar_conteudo_completo(texto)
    if "Erro" in artigo:
        print("❌ Falha ao gerar conteúdo com IA")
        return "Erro na geração de texto", 500

    print("✅ Texto gerado:")
    print(artigo)

    with open("output.html", "w", encoding="utf-8") as f:
        f.write(artigo)

    return "Texto gerado e salvo com sucesso!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
