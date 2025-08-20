
from utils.rss import buscar_noticias
from utils.extrator import extrair_conteudo
from utils.huggingface import gerar_texto_ia
from utils.wordpress import publicar_noticia

print("🔍 Buscando notícias no Google News...")
noticias = buscar_noticias("litoral norte de SP")

for noticia in noticias:
    print(f"📰 Coletando: {noticia}")
    titulo, corpo, imagem_url = extrair_conteudo(noticia)
    if not corpo:
        print("⚠ Falha na extração. Pulando...")
        continue

    texto_gerado = gerar_texto_ia(titulo + "\n\n" + corpo)
    if not texto_gerado:
        print("⚠ Falha na geração. Pulando...")
        continue

    sucesso = publicar_noticia(titulo, texto_gerado, imagem_url)
    if sucesso:
        print("✅ Publicado com sucesso:", titulo)
    else:
        print("❌ Falha na publicação.")
