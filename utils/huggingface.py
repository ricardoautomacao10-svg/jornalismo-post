import requests
import os

API_KEY = os.getenv("HUGGINGFACE_API_KEY") or "hf_SUA_CHAVE_AQUI"

def gerar_texto(prompt):
    url = "https://api-inference.huggingface.co/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "temperature": 0.7,
            "max_new_tokens": 700
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        resultado = response.json()
        if isinstance(resultado, list):
            return resultado[0].get("generated_text", "")
        return resultado.get("generated_text", "")
    else:
        raise Exception(f"Erro na API do Hugging Face: {response.status_code} - {response.text}")
