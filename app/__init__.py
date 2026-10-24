
from flask import Flask, render_template, request
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

        if request.method == "POST":
            cliente = request.form.get("cliente", "").strip()
            telefone = request.form.get("telefone", "").strip()
            produtos = request.form.get("produtos", "").strip()
            data = request.form.get("data", "")
            horario = request.form.get("horario", "")
            tipo = request.form.get("tipo", "")
            observacoes = request.form.get("observacoes", "").strip()

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

            return render_template( 
                "index.html",
                mensagem="Encomenda registrada com sucesso!")
       
        return render_template("nova_encomenda.html", hoje=hoje)

    return app
