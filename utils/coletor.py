
import requests
from newspaper import Article

def buscar_links_do_google_news(query):
    return ["https://www.ubatuba.sp.gov.br/noticias/estudantesiniciam06ago/"]

def extrair_conteudo(url):
    artigo = Article(url, language='pt')
    artigo.download()
    artigo.parse()
    return artigo.title, artigo.text, artigo.top_image
