def entregar_para_plugin(conteudo: dict):
    """
    Salva o conteúdo gerado em um arquivo JSON para que o plugin do WordPress publique.
    """
    import json
    import os
    from datetime import datetime

    pasta_saida = "publicados"
    os.makedirs(pasta_saida, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    nome_arquivo = f"{pasta_saida}/post_{timestamp}.json"

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(conteudo, f, ensure_ascii=False, indent=2)

    print(f"✅ Conteúdo salvo em: {nome_arquivo}")
