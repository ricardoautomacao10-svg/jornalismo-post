import requests

TEXTSYNTH_API_KEY = "3b62b8216593f8593397ed2debb074fc"
TEXTSYNTH_URL = "https://api.textsynth.com/v1/engines/gptj_6B/completions"

def gerar_html_completo(titulo, texto_original, imagem_url):
    prompt = f"Reescreva esse conteúdo como uma matéria jornalística completa para rádio e web, com cerca de 800 palavras, tom objetivo, estilo jornalístico, com SEO, dividida em parágrafos:\n\n{texto_original}\n\nMatéria:"
    headers = {"Authorization": f"Bearer {TEXTSYNTH_API_KEY}"}
    data = {
        "prompt": prompt,
        "max_tokens": 1000,
        "temperature": 0.7
    }
    try:
        response = requests.post(TEXTSYNTH_URL, json=data, headers=headers)
        response.raise_for_status()
        texto_gerado = response.json()["text"]
    except Exception as e:
        texto_gerado = f"<p>Erro ao gerar texto com TextSynth: {str(e)}</p>"

    html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{titulo}</title>
    </head>
    <body>
        <h1>{titulo}</h1>
        {'<img src="' + imagem_url + '" style="max-width:100%;">' if imagem_url else ''}
        <div>{texto_gerado.replace("\n", "<br><br>")}</div>
    </body>
    </html>
    """
    return html
