import requests
import os

TEXTSYNTH_API_KEY = os.getenv("TEXTSYNTH_API_KEY")

def gerar_artigo(titulo, texto):
    prompt = f"Reescreva esse conteúdo como uma matéria jornalística completa para rádio e web, com SEO, título forte e cerca de 800 palavras:\n\n{titulo}\n\n{texto}"

    try:
        response = requests.post(
            "https://api.textsynth.com/v1/engines/gptj_6B/completions",
            headers={"Authorization": f"Bearer {TEXTSYNTH_API_KEY}"},
            json={
                "prompt": prompt,
                "max_tokens": 1000,
                "temperature": 0.7
            }
        )
        response.raise_for_status()
        data = response.json()
        return data.get("text", "Erro: texto não gerado.")
    except Exception as e:
        return f"Erro na geração de texto com TextSynth: {str(e)}"
