from newspaper import Article
from utils.huggingface import gerar_texto

def gerar_conteudo_completo(url: str) -> str:
    artigo = Article(url, language='pt')
    artigo.download()
    artigo.parse()
    conteudo = artigo.text
    prompt = f"Reescreva o seguinte conteúdo como uma notícia para leitura em rádio com cerca de 800 palavras:\n{conteudo}"
    return gerar_texto(prompt)
