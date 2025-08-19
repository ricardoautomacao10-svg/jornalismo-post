import requests

API_URL = "https://api-inference.huggingface.co/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
HEADERS = {"Authorization": "Bearer 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"}

def gerar_conteudo_completo(titulo, texto, imagem):
    prompt = f"Gere uma notícia completa com cerca de 500 a 800 palavras com base no seguinte conteúdo:\n\nTítulo: {titulo}\n\nTexto: {texto}"
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 1024}}
    try:
        resposta = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
        resposta.raise_for_status()
        resultado = resposta.json()
        if isinstance(resultado, list) and "generated_text" in resultado[0]:
            noticia = resultado[0]["generated_text"]
            return {
                "titulo": titulo.strip(),
                "subtitulo": noticia[:120],
                "corpo": f"<img src='{imagem}' /><br><br>{noticia}",
                "imagem": imagem,
                "meta": noticia[:150],
                "categorias": "Litoral Norte",
                "tags": "notícia, litoral, sp"
            }
    except Exception as e:
        print("Erro IA:", e)
        return None