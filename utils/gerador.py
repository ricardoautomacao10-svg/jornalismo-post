from utils.huggingface import gerar_texto

def gerar_conteudo_completo(texto_extraido):
    prompt = f"""Reescreva esse conteúdo como uma matéria jornalística completa para rádio e web, com 800 palavras, mantendo o conteúdo informativo, o contexto local e linguagem jornalística direta. Evite copiar o texto original, reescreva com novas palavras:

{texto_extraido}
"""
    return gerar_texto(prompt)
