
import requests

API_URL = "https://api.textsynth.com/v1/engines/gptj_6B/completions"
API_KEY = "3b62b8216593f8593397ed2debb074fc"

def gerar_artigo_textsynth(titulo, texto_original):
    prompt = f"Reescreva o seguinte conteúdo como uma matéria jornalística completa para rádio e web, com cerca de 800 palavras, linguagem de SEO, tom formal e jornalístico. Mantenha o conteúdo original e aprofunde com contexto:\n\n{texto_original}"

    payload = {
        "prompt": prompt,
        "max_tokens": 800,
        "temperature": 0.7,
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("text", "").strip()
    else:
        raise Exception(f"Erro na geração de texto com TextSynth: {response.status_code} - {response.text}")
