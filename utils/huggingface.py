
import os
import requests

API_URL = "https://api-inference.huggingface.co/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN')}"
}

def gerar_texto(prompt):
    response = requests.post(API_URL, headers=HEADERS, json={
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "messages": [
            {"role": "system", "content": "Você é um jornalista que escreve textos objetivos e bem elaborados para rádio e web."},
            {"role": "user", "content": prompt}
        ]
    })
    if response.status_code != 200:
        raise Exception(f"Erro na geração de texto: {response.status_code} - {response.text}")
    return response.json()["choices"][0]["message"]["content"]
