from newspaper import Article

def extrair_noticia(url):
    try:
        article = Article(url, language='pt')
        article.download()
        article.parse()
        return article.title, article.text
    except Exception as e:
        return "", ""
