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


def gerar_conteudo_completo(conteudo_extraido):
    prompt = (
        f"Reescreva esse conteúdo como uma matéria jornalística completa para rádio e web, "
        f"com aproximadamente 800 palavras, linguagem jornalística direta, informativa e clara, "
        f"sem repetições e sem frases curtas demais. Respeite o conteúdo original mas reescreva como se fosse "
        f"uma lauda jornalística pronta para leitura em rádio:\n\n{conteudo_extraido}"
    )
    return gerar_texto(prompt)


if __name__ == "__main__":
    conteudo = """
    A Prefeitura de Ubatuba, por meio da Secretaria de Educação, iniciou nesta semana o retorno às aulas da rede municipal...
    """
    print("🧠 Gerando conteúdo jornalístico com IA...")
    try:
        resultado = gerar_conteudo_completo(conteudo)
        print("✅ Texto gerado:\n")
        print(resultado)
    except Exception as e:
        print("❌ Falha:", e)
