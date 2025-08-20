from utils.extrator import extrair_conteudo
from utils.gerador import gerar_conteudo_completo
import time

def main():
    print("🔍 Buscando notícias no Google News...")

    # Exemplo fixo (substitua depois com busca dinâmica se quiser)
    urls = [
        "https://www.ubatuba.sp.gov.br/noticias/estudantesiniciam06ago/"
    ]

    for url in urls:
        print(f"📰 Coletando: {url}")
        try:
            titulo, texto, imagem = extrair_conteudo(url)
            print("✅ Extração concluída. Gerando conteúdo...")
            gerar_conteudo_completo(titulo, texto, imagem)
        except Exception as e:
            print(f"⚠ Erro ao processar: {e}")

        time.sleep(5)  # Pausa entre publicações

if __name__ == "__main__":
    main()
