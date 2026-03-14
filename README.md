# 💊 Revolution Suplementos - E-commerce Fictício

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/ac1955fe-84ed-4243-bc31-aa0c88c39c79" />

Este é um projeto de e-commerce básico e fictício desenvolvido para fins de estudo. O objetivo principal foi praticar a estruturação de uma aplicação web utilizando **Django** e realizar o ciclo completo de deploy em um ambiente de produção real.

🚀 **Acesse o projeto online:** [https://revosuplementos.onrender.com/]

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.13** - Linguagem base.
* **Django 5.0** - Framework Web.
* **Gunicorn** - Servidor HTTP WSGI para produção.
* **WhiteNoise** - Servidor de arquivos estáticos.
* **SQLite** - Banco de dados (utilizado para fins de teste/estudo).
* **Render** - Plataforma de Hospedagem (PaaS).

---

## 📋 Funcionalidades do Projeto

* **Catálogo de Produtos:** Exibição dinâmica de suplementos cadastrados via painel administrativo.
* **Gerenciamento de Estoque:** Controle básico de unidades disponíveis com alertas visuais de "Esgotado".
* **Sistema de Reserva:** Fluxo simplificado onde o cliente reserva o produto e é direcionado para finalização via WhatsApp.
* **Painel Administrativo:** Interface completa para gestão de produtos, categorias e reservas.
* **Interface Responsiva:** Layout adaptado para dispositivos móveis e desktop.

---

## 🔧 Configuração Local

Caso queira rodar este projeto localmente, siga os passos abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/RevoSuplementos.git
   cd revosuplementos

Crie e ative um ambiente virtual:

# No Windows:
   ```python
   python -m venv .venv
   ```

Caso o script Activate.ps1 do ambiente virtual do Python esteja sendo barrado pela Execution Policy, execute o seguinte código no PowerShell:

   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
ative a venv:

   ```python
   .venv\Scripts\activate
   ```

# No Linux/Mac:
   ```python
   sudo apt update
   ```

   ```python
   sudo apt install python3-venv
   ```

   ```python
   python3 -m venv .venv
   ```

   ```python
   source .venv/bin/activate
   ```

Instale as dependências:

   ```python
   pip install -r requirements.txt
   ```

Ajuste para Modo de Desenvolvimento (Importante):
Para evitar o Erro 500 localmente, abra o arquivo revosuplementos/settings.py e altere:

Mude DEBUG = False para DEBUG = True.

Garanta que ALLOWED_HOSTS = ['*'] ou inclua 'localhost'.

Execute as migrações e inicie o servidor:

   ```python
   python manage.py migrate
   ```

   ```python
   python manage.py runserver
   ```

   ```python
   Acesse: http://127.0.0.1:8000
   ```

---

🌐 Deploy em Produção
O projeto foi configurado para rodar no Render. As principais configurações realizadas para produção incluem:

Uso do gunicorn para servir a aplicação.

Configuração do whitenoise para gerenciar arquivos CSS, JS e imagens.

Tratamento de variáveis de ambiente para a SECRET_KEY e ALLOWED_HOSTS.

📝 Notas de Estudo
Este projeto é um MVP (Minimum Viable Product) e não possui integração real com gateways de pagamento ou persistência de dados em volumes de disco externos (devido às limitações da camada gratuita do Render). É uma prova de conceito focada em lógica de back-end e infraestrutura.

Desenvolvido por [Lucas Machado] - [https://www.linkedin.com/in/luccas-machhado/]
