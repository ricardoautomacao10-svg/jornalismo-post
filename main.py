import os
import requests

HUGGINGFACE_API_KEY = os.getenv("HF_TOKEN")
MODEL = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"

def gerar_texto(prompt):
    url = f"https://api-inference.huggingface.co/models/{MODEL}"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {"inputs": prompt}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

if __name__ == "__main__":
    prompt = "Escreva uma notícia jornalística sobre a ventania no Litoral Norte de São Paulo."
    resultado = gerar_texto(prompt)
    print(resultado)