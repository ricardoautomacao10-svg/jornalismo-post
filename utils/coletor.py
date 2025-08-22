import time
import requests
from newspaper import Article

def extrair_noticia(url):
    try:
        session = requests.Session()
        session.get(url, timeout=10)
        time.sleep(20)
        artigo = Article(url)
        artigo.download()
        artigo.parse()
        return artigo.title, artigo.text, artigo.top_image or ""
    except Exception as e:
        raise Exception(f"Erro ao extrair a notícia: {str(e)}")
