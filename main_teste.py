from utils.gerador import gerar_conteudo_completo

conteudo = """
A Prefeitura de Ubatuba, por meio da Secretaria de Educação, iniciou nesta semana o retorno às aulas da rede municipal...
"""

print("🧠 Gerando conteúdo jornalístico com IA...")
resultado = gerar_conteudo_completo(conteudo)
print("✅ Texto gerado:\n")
print(resultado)
