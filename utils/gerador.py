import requests

def gerar_artigo_html(titulo, texto, imagem):
    return f"""
    <html>
    <head>
        <title>{titulo}</title>
        <meta name="description" content="{titulo}">
    </head>
    <body>
        <img src="{imagem}" alt="Imagem da notícia" style="max-width: 100%;">
        <h1>{titulo}</h1>
        <p>{texto}</p>
    </body>
    </html>
    """
