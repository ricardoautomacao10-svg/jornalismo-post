from utils.textsynth import gerar_texto

def gerar_conteudo_completo(titulo, corpo):
    prompt = f"""Reescreva esse conteúdo como uma matéria jornalística completa para rádio e web, com cerca de 800 palavras. 
A linguagem deve ser clara, objetiva, informativa, com foco jornalístico. Não use linguagem institucional. A matéria começa agora:

Título: {titulo}

Conteúdo original:
{corpo}

Matéria reescrita:
"""
    return gerar_texto(prompt)
