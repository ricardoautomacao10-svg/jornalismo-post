from newspaper import Article

def extrair_noticia(url):
    try:
        artigo = Article(url, language='pt')
        artigo.download()
        artigo.parse()
        return artigo.title, artigo.text, artigo.top_image
    except Exception as e:
        print(f"Erro ao extrair notícia: {e}")
        return None, None, None
