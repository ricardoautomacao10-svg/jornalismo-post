import os
import requests

HF_API_URL = "https://api-inference.huggingface.co/v1/chat/completions"
HF_API_KEY = os.environ.get("HF_TOKEN")

def gerar_texto(prompt):
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}"
    }
    payload = {
        "model": "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B:nscale",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(HF_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Erro na geração de texto: {response.status_code} - {response.text}")
