# utils/coletor.py
import requests
from newspaper import Article

def coletar_noticia(url):
    try:
        artigo = Article(url, language='pt')
        artigo.download()
        artigo.parse()
        return artigo.title, artigo.text
    except Exception as e:
        print(f"Erro ao coletar a notícia: {e}")
        return None, None

# utils/gerador.py
from utils.textsynth import gerar_texto_textsynth

def gerar_conteudo_completo(titulo, conteudo_original):
    prompt = f"""
Reescreva a seguinte matéria como uma reportagem jornalística completa para rádio e web, com linguagem informativa, cerca de 800 palavras, tom jornalístico, e estrutura de manchete, lide e desenvolvimento:

Título: {titulo}

Conteúdo original:
{conteudo_original}
    """
    return gerar_texto_textsynth(prompt)

# utils/textsynth.py
import os
import requests

def gerar_texto_textsynth(prompt):
    api_key = os.getenv("TEXTSYNTH_KEY")
    if not api_key:
        return "Erro: TEXTSYNTH_KEY não configurada."

    url = "https://api.textsynth.com/v1/engines/gptj_6B/completions"
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {
        "prompt": prompt,
        "max_tokens": 1024,
        "temperature": 0.7,
        "top_p": 0.9,
        "stop": ["</s>"]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json().get("text", "Erro: Resposta vazia da API.")
    except Exception as e:
        return f"Erro ao gerar texto com TextSynth: {e}"

# requirements.txt
newspaper3k
requests
