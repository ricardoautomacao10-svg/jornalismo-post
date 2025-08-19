import requests
import time
from utils.rss import buscar_links_google_news, buscar_links_rss
from utils.extrator import extrair_conteudo
from utils.huggingface import gerar_conteudo_completo
from utils.wordpress import enviar_para_plugin

PALAVRAS_CHAVE = ["litoral norte de SP", "ubatuba", "ilhabela", "caraguatatuba", "são sebastião"]

def processar_noticias():
    print("🔍 Buscando notícias no Google News...")
    links = buscar_links_google_news(PALAVRAS_CHAVE)
    if not links:
        print("⚠ Nada no Google News. Buscando nos RSS...")
        links = buscar_links_rss()
    if not links:
        print("❌ Nenhuma notícia encontrada.")
        return

    for link in links:
        print(f"📰 Coletando: {link}")
        time.sleep(10)
        titulo, texto, imagem = extrair_conteudo(link)
        if not texto:
            print("⚠ Falha na extração. Pulando...")
            continue

        print("🤖 Gerando conteúdo com IA...")
        dados = gerar_conteudo_completo(titulo, texto, imagem)
        if not dados:
            print("⚠ Erro na IA. Pulando...")
            continue

        print("📤 Enviando ao WordPress...")
        enviado = enviar_para_plugin(dados)
        if enviado:
            print("✅ Publicado com sucesso!\n")
            break

if __name__ == "__main__":
    processar_noticias()
