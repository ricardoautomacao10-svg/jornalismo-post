from utils.huggingface import gerar_texto

def gerar_conteudo_completo(texto):
    prompt = f"Reescreva esse conteúdo como uma matéria jornalística completa para rádio e web, com 800 palavras:

{texto}"
    return gerar_texto(prompt)
