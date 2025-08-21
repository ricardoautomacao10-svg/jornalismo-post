from utils.coletor import extrair_noticia
from utils.gerador import gerar_conteudo_completo

url = "https://www.ubatuba.sp.gov.br/noticias/estudantesiniciam06ago/"

print("🔍 Buscando notícias no Google News...")
print(f"📰 Coletando: {url}")

titulo, conteudo = extrair_noticia(url)

if conteudo:
    print("✅ Extração concluída. Gerando conteúdo...")
    texto_final = gerar_conteudo_completo(titulo, conteudo)
    print("✅ Texto gerado:")
    print(texto_final)
else:
    print("❌ Falha na extração de conteúdo.")
