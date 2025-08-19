import requests

PLUGIN_URL = "https://jornalvozdolitoral.com/wp-json/custom-plugin/v1/publicar"

def enviar_para_plugin(dados):
    try:
        resposta = requests.post(PLUGIN_URL, json=dados, timeout=30)
        return resposta.status_code == 200
    except Exception as e:
        print("Erro WordPress:", e)
        return False