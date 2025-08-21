import requests

API_URL = "https://api.textsynth.com/v1/engines/gptj_6B/completions"

def gerar_texto(prompt: str) -> str:
    payload = {
        "prompt": prompt,
        "max_tokens": 1024,
        "temperature": 0.7,
        "top_p": 0.9,
    }

    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        resultado = response.json()
        return resultado.get("text", "").strip()

    except Exception as e:
        print(f"Erro na geração de texto com TextSynth: {e}")
        return "Erro ao gerar texto com TextSynth."
