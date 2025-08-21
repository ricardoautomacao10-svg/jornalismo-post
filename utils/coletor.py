from newspaper import Article

def extrair_noticia(url):
    article = Article(url, language="pt")
    article.download()
    article.parse()
    if not article.title or not article.text:
        raise ValueError("Conteúdo incompleto extraído.")
    return article.title, article.text, article.top_image or ""
