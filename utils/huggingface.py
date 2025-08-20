import os
import requests

def gerar_texto(prompt):
    token = os.environ.get("HF_TOKEN")

    if not token:
        raise ValueError("Token Hugging Face não encontrado. Defina HF_TOKEN nas variáveis de ambiente.")

    url = "https://api-inference.huggingface.co/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    data = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 600,
            "temperature": 0.7
        }
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code != 200:
        raise RuntimeError(f"Erro na geração de texto: {response.status_code} - {response.text}")

    resultado = response.json()
    return resultado[0]["generated_text"]
