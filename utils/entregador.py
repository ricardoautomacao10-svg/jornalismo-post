from utils.wordpress import publicar_no_wordpress

def entregar_para_plugin(conteudo_dict):
    titulo = conteudo_dict.get("titulo")
    corpo = conteudo_dict.get("corpo")
    categorias = conteudo_dict.get("categorias", [1])
    tags = conteudo_dict.get("tags", [])
    imagem = conteudo_dict.get("imagem")

    resultado = publicar_no_wordpress(
        titulo=titulo,
        conteudo=corpo,
        categorias=categorias,
        tags=tags,
        imagem_url=imagem
    )

    return resultado
# entregador.py (coloque aqui a função entregar_para_plugin real)
