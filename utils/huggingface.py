from utils.gerador import gerar_conteudo_completo

if __name__ == "__main__":
    url = "https://www.ubatuba.sp.gov.br/noticias/estudantesiniciam06ago/"
    conteudo = gerar_conteudo_completo(url)
    print(conteudo)
