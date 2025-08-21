import os
import requests

def gerar_texto(prompt: str) -> str:
    API_URL = "https://api-inference.huggingface.co/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
    headers = {
        "Authorization": f"Bearer {os.environ['HF_TOKEN']}"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 512,
            "do_sample": True,
            "temperature": 0.7
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception(f"Erro na geração de texto: {response.status_code} - {response.text}")
    return response.json()[0]['generated_text']
