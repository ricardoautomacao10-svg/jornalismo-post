import requests

API_URL = "https://api.cohere.ai/v1/generate"
API_KEY = "YOUR_API_KEY"

def gerar_artigo_html(titulo, texto, imagem_url):
    prompt = f"Reescreva esse conteúdo como uma matéria jornalística completa para rádio e web, com cerca de 800 palavras, estilo SEO e com linguagem natural:\n\n{texto}"

    resposta = requests.post(API_URL,
        headers={{
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }},
        json={{
            "model": "command-r-plus",
            "prompt": prompt,
            "max_tokens": 1500
        }}
    )

    resposta.raise_for_status()
    saida = resposta.json()["generations"][0]["text"].strip()

    html = "<html><head><meta charset='utf-8'><title>{}</title></head><body>".format(titulo)
    html += "<h1>{}</h1>".format(titulo)
    html += f"<img src='{imagem_url}' style='max-width:100%;'><br><br>"
    html += "<p>{}</p>".format(saida.replace("\n", "<br>"))
    html += "</body></html>"
    return html
