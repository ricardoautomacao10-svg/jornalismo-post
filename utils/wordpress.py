import requests

def publicar_no_wordpress(titulo, conteudo, categorias, tags, imagem_url):
    url = "https://jornalvozdolitoral.com/wp-json/wp/v2/posts"
    user = "GeradorRSS"
    senha = "l$qy7qgZvZhUya1kynBk5zte"

    # Define categorias e tags (você pode adaptar para IDs diferentes)
    categoria_ids = categorias or [1]  # 1 = Padrão
    tag_names = tags or []

    # Conteúdo final com imagem no topo
    conteudo_html = f'<img src="{imagem_url}" alt="{titulo}"/><br><br>{conteudo}'

    headers = {
        "Content-Type": "application/json"
    }

    post = {
        "title": titulo,
        "content": conteudo_html,
        "status": "publish",
        "categories": categoria_ids,
        "tags": tag_names
    }

    response = requests.post(url, json=post, headers=headers, auth=(user, senha))

    if response.status_code == 201:
        print("✅ Publicado com sucesso no WordPress!")
        return response.json()
    else:
        print(f"❌ Erro ao publicar: {response.status_code}")
        print(response.text)
        return None
