import requests
import os

def gerar_texto_jornalistico(titulo, texto_original):
    prompt = f"""
Reescreva esse conteúdo como uma matéria jornalística completa para rádio e web, com 800 palavras, tom jornalístico, sem exageros, focado em SEO Google. Use este título como base: {titulo}. 
Conteúdo original: {texto_original}
"""

    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 800},
    }

    headers = {
        "Authorization": f"Bearer {os.environ.get('HF_TOKEN')}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            "https://api-inference.huggingface.co/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
            headers=headers,
            json=payload,
            timeout=60
        )
        response.raise_for_status()
        resultado = response.json()
        return resultado[0]["generated_text"]
    except Exception as e:
        print(f"Erro na geração de texto com Hugging Face: {e}")
        return None
