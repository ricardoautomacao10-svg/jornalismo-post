import requests

TEXTSYNTH_API_URL = "https://api.textsynth.com/v1/engines/gptj_6B/completions"
API_KEY = "3b62b8216593f8593397ed2debb074fc"

def gerar_texto_completo(titulo, texto_base, imagem_url):
    prompt = f"""
Reescreva esse conteúdo como uma matéria jornalística completa, com cerca de 800 palavras, pronta para leitura em rádio e publicação na web. Use um tom informativo, direto e bem estruturado. Mantenha o foco nos fatos e adicione contexto onde necessário.

Título: {titulo}

Conteúdo original:
{texto_base}

Matéria final:
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "prompt": prompt,
        "max_tokens": 1024,
        "temperature": 0.7
    }

    response = requests.post(TEXTSYNTH_API_URL, json=data, headers=headers)
    if response.status_code == 200:
        texto_gerado = response.json().get("text", "Erro ao gerar texto.")
    else:
        texto_gerado = f"Erro na geração de texto com TextSynth: {response.status_code} - {response.text}"

    html = f"""
    <html>
    <head><meta charset="utf-8"><title>{titulo}</title></head>
    <body>
        <h1>{titulo}</h1>
        {'<img src="' + imagem_url + '" width="100%" />' if imagem_url else ''}
        <p>{texto_gerado.replace('\\n', '<br><br>')}</p>
    </body>
    </html>
    """
    return html
