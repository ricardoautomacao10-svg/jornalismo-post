
import os
import re

def limpar_titulo(titulo):
    return re.sub(r'[^a-zA-Z0-9_-]', '', titulo.replace(' ', '_'))

def salvar_html(titulo, texto, imagem_url):
    nome_arquivo = limpar_titulo(titulo) + ".html"
    caminho = os.path.join("/tmp", nome_arquivo)
    
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(f"<html><head><meta charset='utf-8'><title>{titulo}</title></head><body>")
        f.write(f"<h1>{titulo}</h1>")
        if imagem_url:
            f.write(f"<img src='{imagem_url}' style='max-width:100%;height:auto;'>")
        f.write(f"<p>{texto.replace('\n', '<br><br>')}</p>")
        f.write("</body></html>")
    return caminho
