
from utils.gerador import gerar_conteudo_completo
from utils.entregador import entregar_para_plugin
from utils.coletor import buscar_links_do_google_news, extrair_conteudo

if __name__ == "__main__":
    print("🔍 Buscando notícias no Google News...")
    links = buscar_links_do_google_news("litoral norte de SP")

    for link in links:
        print(f"📰 Coletando: {link}")
        try:
            titulo, texto, imagem = extrair_conteudo(link)
            print("✅ Extração concluída. Gerando conteúdo...")
            resultado = gerar_conteudo_completo(texto)
            entregar_para_plugin(titulo, resultado, imagem)
        except Exception as e:
            print(f"⚠ Erro ao processar: {e}")
