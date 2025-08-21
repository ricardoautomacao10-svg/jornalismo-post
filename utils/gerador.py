import requests

API_URL = "https://api.textsynth.com/v1/engines/gptj_6B/completions"
API_KEY = "3b62b8216593f8593397ed2debb074fc"

def gerar_texto(titulo, conteudo):
    prompt = f"Reescreva como uma matéria jornalística completa para rádio e web, com 800 palavras, com base no título e conteúdo a seguir:\nTítulo: {titulo}\nConteúdo original: {conteudo}\n\nMatéria final:"

    payload = {
        "prompt": prompt,
        "max_tokens": 1024,
        "temperature": 0.7
    }

    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()["text"]
    else:
        raise Exception("Erro na geração de texto com TextSynth")
