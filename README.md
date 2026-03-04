🏋️‍♂️ RevoSuplementos








Sistema web desenvolvido com Django para gerenciamento de uma loja de suplementos.
O projeto segue boas práticas de organização e estrutura padrão do framework.

🔗 Repositório oficial no GitHub

📌 Sobre o Projeto

O RevoSuplementos é uma aplicação web construída com foco em:

Estrutura organizada

Separação de responsabilidades

Escalabilidade

Boas práticas do Django

O sistema pode ser expandido para incluir:

Cadastro de produtos

Carrinho de compras

Sistema de pedidos

Painel administrativo

Upload de imagens

Controle de estoque

🧠 Tecnologias Utilizadas
🐍 Python

Linguagem principal do projeto.
Responsável por toda a lógica da aplicação e backend.

🌿 Django

Framework web de alto nível que permite:

Roteamento automático

ORM integrado

Sistema de autenticação

Segurança contra SQL Injection e CSRF

Admin Panel pronto para uso

Estrutura MVC (MTV no Django)

O projeto segue a arquitetura:

Model → Template → View
🗄 SQLite

Banco de dados padrão utilizado durante o desenvolvimento.

Vantagens:

Leve

Fácil configuração

Ideal para projetos em fase inicial

Pode ser facilmente substituído por:

PostgreSQL

MySQL

Outro banco relacional em produção

🎨 Static Files

Gerenciamento de:

CSS

JavaScript

Imagens

Arquivos estáticos

Utiliza a estrutura padrão do Django com staticfiles/ e media/.

📂 Estrutura do Projeto
RevoSuplementos/
│
├── manage.py
├── requirements.txt
├── runtime.txt
├── db.sqlite3
├── staticfiles/
│
├── revosuplementos/
│   ├── loja/              # App principal
│   ├── media/             # Arquivos enviados
│   └── revosuplementos/   # Configurações do projeto
│       ├── settings.py
│       ├── urls.py
│       ├── wsgi.py
│       └── asgi.py
