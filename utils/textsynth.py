import os
import requests

def gerar_texto(prompt):
    api_key = os.environ.get("TEXTSYNTH_KEY")
    if not api_key:
        return "Erro: TEXTSYNTH_KEY não configurada."

    url = "https://api.textsynth.com/v1/engines/gptj_6B/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 1024,
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json().get("text", "").strip()
    except Exception as e:
        return f"Erro ao gerar texto com TextSynth: {e}"
