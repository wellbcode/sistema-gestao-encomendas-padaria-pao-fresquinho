
from app.models.encomenda import criar_encomenda


def test_criar_encomenda_com_dados_corretos():
    encomenda = criar_encomenda(
        cliente="Maria Silva",
        telefone="11999999999",
        produtos="Bolo de chocolate",
        data="25/10/2026",
        horario="14:00",
        tipo="Retirada",
        observacoes="Sem granulado"
    )

    assert encomenda["cliente"] == "Maria Silva"
    assert encomenda["telefone"] == "11999999999"
    assert encomenda["produtos"] == "Bolo de chocolate"
    assert encomenda["data"] == "25/10/2026"
    assert encomenda["horario"] == "14:00"
    assert encomenda["tipo"] == "Retirada"
    assert encomenda["observacoes"] == "Sem granulado"


def test_nova_encomenda_comeca_com_status_recebida():
    encomenda = criar_encomenda(
        cliente="João Santos",
        telefone="11988888888",
        produtos="Pão de queijo",
        data="26/10/2026",
        horario="09:00",
        tipo="Entrega"
    )

    assert encomenda["status"] == "Recebida"


def test_encomenda_tem_identificador_e_data_de_criacao():
    encomenda = criar_encomenda(
        cliente="Ana Souza",
        telefone="11977777777",
        produtos="Torta de limão",
        data="27/10/2026",
        horario="16:00",
        tipo="Retirada"
    )

    assert encomenda["id"]
    assert encomenda["criada_em"]

from app import create_app
from pathlib import Path
import app.models.armazenamento as armazenamento


def test_nao_permite_cadastrar_encomenda_sem_cliente(
    tmp_path, monkeypatch
):
    arquivo_teste = tmp_path / "encomendas.json"

    monkeypatch.setattr(
        armazenamento,
        "ARQUIVO_ENCOMENDAS",
        arquivo_teste
    )

    app = create_app()
    app.config["TESTING"] = True

    cliente = app.test_client()

    resposta = cliente.post(
        "/nova-encomenda",
        data={
            "cliente": "",
            "telefone": "",
            "produtos": "Bolo de chocolate",
            "data": "2026-10-25",
            "horario": "14:00",
            "tipo": "Retirada",
            "observacoes": ""
        }
    )

    assert resposta.status_code == 400
    assert b"Informe o nome do cliente." in resposta.data
    assert not arquivo_teste.exists()
