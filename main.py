from utils.gerador import gerar_conteudo_completo

if __name__ == "__main__":
    url = "https://www.ubatuba.sp.gov.br/noticias/estudantesiniciam06ago/"
    print("🔍 Buscando notícias no Google News...")
    print(f"📰 Coletando: {url}")
    try:
        texto = gerar_conteudo_completo(url)
        print("✅ Texto gerado:\n")
        print(texto)
    except Exception as e:
        print(f"⚠ Erro ao processar: {e}")
