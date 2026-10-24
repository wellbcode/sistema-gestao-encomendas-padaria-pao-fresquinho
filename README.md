# Sistema de Gestão de Encomendas — Padaria Pão Fresquinho

## Sobre o projeto

O Sistema de Gestão de Encomendas da Padaria Pão Fresquinho é um MVP desenvolvido para centralizar e organizar os pedidos de uma pequena padaria, facilitando o registro, a consulta e o acompanhamento das encomendas.

## Objetivo

Reduzir a dependência de anotações em papel e mensagens dispersas, tornando o controle dos pedidos mais simples e organizado.

## Funcionalidades implementadas

- Cadastro de novas encomendas.
- Visualização das encomendas cadastradas.
- Atualização do status dos pedidos.
- Acompanhamento das etapas: recebida, em preparação, pronta para entrega e entregue.

## Validação e testes

O sistema realiza validações no cadastro de encomendas para impedir o envio de informações obrigatórias ausentes ou inválidas.

O projeto também possui testes automatizados com `pytest` para verificar a criação das encomendas e o comportamento esperado das funcionalidades.

Para executar os testes, utilize o comando:

```bash
python -m pytest -v
```

## Tecnologias utilizadas

- Python
- Flask
- HTML
- CSS
- Git e GitHub para versionamento do código.

## Como executar o projeto

1. Instale o Python.
2. Abra o terminal na pasta do projeto.
3. Crie e ative um ambiente virtual, se ainda não tiver um:

   ```bash
   python -m venv venv
   ```

   No Windows PowerShell, ative-o com:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

4. Instale o Flask:

   ```bash
   pip install Flask
   ```

5. Inicie a aplicação conforme a configuração do arquivo `app/__init__.py`.

## Status do projeto

MVP em desenvolvimento, com cadastro e acompanhamento do status das encomendas.

## Repositório

[GitHub — Sistema de Gestão de Encomendas da Padaria Pão Fresquinho](https://github.com/wellbcode/sistema-gestao-encomendas-padaria-pao-fresquinho.git)
