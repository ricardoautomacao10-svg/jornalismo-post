
import requests
from bs4 import BeautifulSoup
from newspaper import Article

def extrair_conteudo(url):
    try:
        artigo = Article(url, language='pt')
        artigo.download()
        artigo.parse()
        return artigo.title, artigo.text, artigo.top_image
    except Exception:
        return None, None, None
