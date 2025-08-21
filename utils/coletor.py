from newspaper import Article

def extrair_noticia(url):
    artigo = Article(url, language="pt")
    artigo.download()
    artigo.parse()

    titulo = artigo.title
    texto = artigo.text
    imagem = artigo.top_image if artigo.top_image else ""

    return titulo, texto, imagem
