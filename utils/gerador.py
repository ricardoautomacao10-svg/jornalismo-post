from utils.extrator import extrair_conteudo
from utils.huggingface import gerar_texto
from utils.wordpress import publicar_no_wordpress

def gerar_conteudo_completo(url):
    print(f"📰 Coletando: {url}")
    
    try:
        titulo, imagem_url, texto_original = extrair_conteudo(url)
        if not texto_original:
            print("⚠ Conteúdo vazio. Pulando...")
            return

        prompt = f"Reescreva a seguinte notícia para um portal local, mantendo um tom jornalístico, com cerca de 700 palavras:\n\n{texto_original}"
        texto_gerado = gerar_texto(prompt)

        conteudo_formatado = f"<img src='{imagem_url}'><h2>{titulo}</h2><p>{texto_gerado}</p>"
        
        publicar_no_wordpress(titulo, conteudo_formatado)

    except Exception as e:
        print(f"❌ Erro ao gerar conteúdo: {e}")
# gerador.py (coloque aqui a função gerar_conteudo_completo real)
