import requests

def gerar_texto_completo(titulo, texto_original):
    prompt = f"Reescreva esse conteúdo como uma matéria jornalística completa para rádio e web com 800 palavras, linguagem jornalística, título: {titulo}\n\n{texto_original}"

    response = requests.post(
        "https://api.textsynth.com/v1/engines/gptj_6B/completions",
        headers={"Authorization": "Bearer 3b62b8216593f8593397ed2debb074fc"},
        json={"prompt": prompt, "max_tokens": 800}
    )
    if response.status_code == 200:
        return response.json()["text"]
    else:
        raise Exception("Erro ao gerar texto com TextSynth: " + response.text)
