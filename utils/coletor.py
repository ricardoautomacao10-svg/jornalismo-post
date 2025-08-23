import time
from newspaper import Article

def extrair_noticia(url):
    artigo = Article(url, language="pt")
    artigo.download()
    time.sleep(20)
    artigo.parse()

    if not artigo.text or not artigo.title:
        raise ValueError("Conteúdo da notícia não pôde ser extraído")

    imagem = artigo.top_image or ""
    return artigo.title, artigo.text, imagem
