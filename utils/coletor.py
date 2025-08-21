from newspaper import Article

def extrair_noticia(url):
    artigo = Article(url, language='pt')
    artigo.download()
    artigo.parse()

    titulo = artigo.title or "Sem título"
    texto = artigo.text or "Sem conteúdo"
    imagem = artigo.top_image if artigo.top_image else ""

    return titulo, texto, imagem
