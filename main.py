from utils.gerador import gerar_conteudo_completo
from utils.extrator import extrair_conteudo
from utils.entregador import entregar_para_plugin

if __name__ == "__main__":
    print("🔍 Buscando notícias no Google News...")

    url = "https://www.ubatuba.sp.gov.br/noticias/estudantesiniciam06ago/"
    try:
        print(f"📰 Coletando: {url}")
        noticia = extrair_conteudo(url)
        print("✅ Extração concluída. Gerando conteúdo...")

        titulo, corpo, tags = gerar_conteudo_completo(noticia)

        entregar_para_plugin(
            titulo=titulo,
            corpo=corpo,
            tags=tags
        )

    except Exception as e:
        print(f"⚠ Erro ao processar: {e}")
