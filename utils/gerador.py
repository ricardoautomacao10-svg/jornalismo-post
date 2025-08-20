from utils.huggingface import gerar_texto
from utils.entregador import entregar_para_plugin

def gerar_conteudo_completo(titulo, texto, imagem):
    # Gera texto com IA (se quiser complementar o conteúdo original)
    corpo_gerado = gerar_texto(texto)

    # Monta HTML final com imagem no topo
    html = f"<h1>{titulo}</h1>\n"
    if imagem:
        html += f"<img src='{imagem}' alt='imagem da matéria' style='max-width:100%;'/>\n"
    html += f"<p>{corpo_gerado}</p>"

    # Envia para o plugin do WordPress
    entregar_para_plugin(
        titulo=titulo,
        subtitulo=titulo,  # Pode ser ajustado se quiser gerar diferente
        corpo=html,
        imagem=imagem
    )
