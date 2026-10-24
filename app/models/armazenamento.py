
import json
from pathlib import Path


ARQUIVO_ENCOMENDAS = Path(__file__).resolve().parent.parent / "encomendas.json"


def carregar_encomendas():
    if not ARQUIVO_ENCOMENDAS.exists():
        return []

    with open(ARQUIVO_ENCOMENDAS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_encomenda(encomenda):
    encomendas = carregar_encomendas()
    encomendas.append(encomenda)

    with open(ARQUIVO_ENCOMENDAS, "w", encoding="utf-8") as arquivo:
        json.dump(encomendas, arquivo, ensure_ascii=False, indent=4)
