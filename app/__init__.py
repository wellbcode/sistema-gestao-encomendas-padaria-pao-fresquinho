
from flask import Flask, render_template, request, redirect
from datetime import date

from app.models.encomenda import criar_encomenda
from app.models.armazenamento import salvar_encomenda, carregar_encomendas


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def inicio():
        encomendas = carregar_encomendas()
        total_encomendas = len(encomendas)
        
        em_preparacao = sum(
            1 for encomenda in encomendas
            if encomenda["status"] == "Em preparação"
        )

        prontas_entrega = sum(
            1 for encomenda in encomendas
            if encomenda["status"] == "Pronta para entrega"
        )

        return render_template(
            "index.html",
            encomendas=encomendas,
            total_encomendas=total_encomendas,
            em_preparacao=em_preparacao,
            prontas_entrega=prontas_entrega
        )
  
    @app.route("/nova-encomenda", methods=["GET", "POST"])
    def nova_encomenda():
        hoje = date.today().isoformat()
        erro = None

        if request.method == "POST":
            cliente = request.form.get("cliente", "").strip()
            telefone = request.form.get("telefone", "").strip()
            produtos = request.form.get("produtos", "").strip()
            data = request.form.get("data", "").strip()
            horario = request.form.get("horario", "").strip()
            tipo = request.form.get("tipo", "").strip()
            observacoes = request.form.get("observacoes", "").strip()

            if not cliente:
                erro = "Informe o nome do cliente."
            elif not produtos:
                erro = "Informe os produtos encomendados."
            elif not data:
                erro = "Informe a data da encomenda."
            elif data < hoje:
                erro = "A data da encomenda não pode ser anterior a hoje."
            elif not horario:
                erro = "Informe o horário."
            elif tipo not in ["Retirada", "Entrega"]:
                erro = "Selecione uma forma de recebimento válida."

            if erro:
                return render_template(
                    "nova_encomenda.html",
                    hoje=hoje,
                    erro=erro
                ), 400

            encomenda = criar_encomenda(
                cliente,
                telefone,
                produtos,
                data,
                horario,
                tipo,
                observacoes
            )

            salvar_encomenda(encomenda)

            return redirect("/")

        return render_template(
            "nova_encomenda.html",
            hoje=hoje,
            erro=erro
        )

    @app.route("/atualizar-status/<id>", methods=["POST"])
    def atualizar_status(id):
        encomendas = carregar_encomendas()

        status_permitidos = [
            "Recebida",
            "Em preparação",
            "Pronta para entrega",
            "Entregue"
        ]

        novo_status = request.form.get("status", "")

        if novo_status not in status_permitidos:
            return "Status inválido", 400

        for encomenda in encomendas:
            if encomenda["id"] == id:
                encomenda["status"] = novo_status
                break
        else:
            return "Encomenda não encontrada", 404

        from app.models.armazenamento import ARQUIVO_ENCOMENDAS
        import json

        with open(ARQUIVO_ENCOMENDAS, "w", encoding="utf-8") as arquivo:
            json.dump(encomendas, arquivo, ensure_ascii=False, indent=4)

        return redirect("/")


    return app
