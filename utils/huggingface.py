
import requests
import os

API_URL = "https://api-inference.huggingface.co/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
API_KEY = os.getenv("HUGGINGFACE_API_KEY") or "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"

def gerar_texto_ia(texto):
    payload = {
        "inputs": texto,
        "parameters": {"max_new_tokens": 700}
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        resposta = response.json()
        return resposta[0]["generated_text"] if isinstance(resposta, list) else resposta.get("generated_text")
    except Exception as e:
        print("Erro IA:", e)
        return None
