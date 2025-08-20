from utils.huggingface import gerar_texto
from utils.wordpress import publicar_no_wordpress
from utils.entregador import entregar_para_plugin

def gerar_conteudo_completo(titulo, texto, imagem):
    """
    Gera o conteúdo completo com base no texto extraído, usando IA e formata para publicação.
    """
    print("🤖 Gerando texto com Hugging Face...")
    corpo_formatado = gerar_texto(texto)

    post = {
        "title": titulo,
        "content": f"<img src='{imagem}'/><br><br>{corpo_formatado}",
        "excerpt": titulo,
        "categories": [116],  # Exemplo: Caraguatatuba
        "tags": ["notícia", "atualidade"],
        "status": "publish"
    }

    entregar_para_plugin(post)
