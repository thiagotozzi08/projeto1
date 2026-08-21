import json

def load_data(nome_arquivo):
    caminho = f"static/data/{nome_arquivo}"
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return dados

def load_template(nome_arquivo):
    caminho = f"static/templates/{nome_arquivo}"
    with open(caminho, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    return conteudo

def save_data(nome_arquivo, dados):
    caminho = f"static/data/{nome_arquivo}"
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)