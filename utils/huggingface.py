import requests
import os

API_KEY = os.getenv("HUGGINGFACE_API_KEY") or "hf_..."

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
        data = response.json()
        if isinstance(data, list):
            return data[0].get("generated_text", "")
        else:
            return data.get("generated_text", "")
    else:
        raise Exception(f"Erro na geração de texto: {response.status_code} - {response.text}")
