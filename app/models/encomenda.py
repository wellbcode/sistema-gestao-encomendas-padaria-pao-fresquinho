
from datetime import datetime


def criar_encomenda(
    cliente,
    telefone,
    produtos,
    data,
    horario,
    tipo,
    observacoes=""
):
    encomenda = {
        "id": datetime.now().strftime("%Y%m%d%H%M%S%f"),
        "cliente": cliente,
        "telefone": telefone,
        "produtos": produtos,
        "data": data,
        "horario": horario,
        "tipo": tipo,
        "observacoes": observacoes,
        "status": "Recebida",
        "criada_em": datetime.now().isoformat(timespec="seconds")
    }

    return encomenda
