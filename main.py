
from utils.extrator import extrair_conteudo
from utils.gerador import gerar_conteudo_completo
from utils.entregador import entregar_para_plugin

if __name__ == "__main__":
    print("🔍 Buscando notícias no Google News...")
    url = "https://www.ubatuba.sp.gov.br/noticias/estudantesiniciam06ago/"  # Exemplo real
    print(f"📰 Coletando: {url}")
    try:
        titulo, imagem, corpo = extrair_conteudo(url)
        print("✅ Extração concluída. Gerando conteúdo...")
        texto_formatado = gerar_conteudo_completo(titulo, imagem, corpo)
        print("🚀 Entregando ao plugin WordPress...")
        entregar_para_plugin(texto_formatado)
        print("✅ Publicação finalizada com sucesso.")
    except Exception as e:
        print(f"⚠ Erro ao processar: {e}")
