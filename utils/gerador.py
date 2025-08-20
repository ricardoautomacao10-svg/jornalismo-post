from utils.huggingface import gerar_texto

def gerar_conteudo_completo(texto_original):
    prompt = (
        "Reescreva o texto a seguir com linguagem jornalística para rádio, "
        "mantendo os fatos, aprofundando a análise e removendo links e repetições:\n\n"
        f"{texto_original}"
    )

    resposta = gerar_texto(prompt)
    titulo = resposta.split("\n")[0].strip()
    corpo = resposta.strip()
    tags = ["Ubatuba", "Educação", "Região", "Notícias"]

    return titulo, corpo, tags
