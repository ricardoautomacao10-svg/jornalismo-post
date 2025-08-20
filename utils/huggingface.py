import os
import requests

HF_API_TOKEN = os.getenv("HF_TOKEN")
MODEL = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
URL = f"https://api-inference.huggingface.co/models/{MODEL}"

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

def gerar_texto(prompt):
    response = requests.post(URL, headers=headers, json={"inputs": prompt})
    
    if response.status_code != 200:
        raise Exception(f"Erro na geração de texto: {response.status_code} - {response.text}")

    resultado = response.json()

    if isinstance(resultado, list) and len(resultado) > 0:
        return resultado[0]["generated_text"]
    elif isinstance(resultado, dict) and "generated_text" in resultado:
        return resultado["generated_text"]
    else:
        return "[ERRO] Texto não gerado."
