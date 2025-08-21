import requests

def gerar_artigo_completo(titulo, texto):
    API_KEY = "3b62b8216593f8593397ed2debb074fc"
    endpoint = "https://api.textsynth.com/v1/engines/gptj_6B/completions"
    prompt = f"Reescreva esse conteúdo como uma matéria jornalística completa para rádio e web, com cerca de 800 palavras, título: {titulo}. Conteúdo original: {texto}"

    response = requests.post(endpoint, json={
        "prompt": prompt,
        "max_tokens": 800,
        "temperature": 0.7,
        "top_p": 0.9,
    }, headers={"Authorization": f"Bearer {API_KEY}"})
    
    if response.status_code == 200:
        return response.json().get("text", "Erro: resposta vazia da IA.")
    else:
        raise Exception(f"Erro na geração de texto com TextSynth: {response.status_code} - {response.text}")
