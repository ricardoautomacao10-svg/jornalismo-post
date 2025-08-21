import os
import requests

API_URL = "https://api-inference.huggingface.co/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
headers = {
    "Authorization": f"Bearer {os.environ.get('HF_TOKEN')}"
}

def gerar_texto(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 800}
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code != 200:
        raise Exception(f"Erro na geração de texto: {response.status_code} - {response.text}")
    
    output = response.json()
    return output[0]["generated_text"] if isinstance(output, list) else output.get("generated_text", "")
