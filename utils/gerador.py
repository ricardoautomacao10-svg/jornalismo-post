from utils.huggingface import gerar_texto

def gerar_conteudo_completo(conteudo_extraido):
    prompt = (
        f"Reescreva esse conteúdo como uma matéria jornalística completa para rádio e web, "
        f"com aproximadamente 800 palavras, linguagem jornalística direta, informativa e clara, "
        f"sem repetições e sem frases curtas demais. Respeite o conteúdo original mas reescreva como se fosse "
        f"uma lauda jornalística pronta para leitura em rádio:\n\n{conteudo_extraido}"
    )
    return gerar_texto(prompt)
