🕵️‍♂️ Price Watcher (macOS Edition)
Um monitor de preços automatizado que rastreia valores em e-commerce e notifica nativamente no macOS quando detecta uma queda de preço.

📖 Sobre o Projeto
Este projeto é uma ferramenta de automação desenvolvida em Python para monitorar flutuações de preços em sites de vendas. Atualmente configurado para ambiente de testes (Scraping Sandbox), o sistema simula um navegador real, captura dados estruturados, armazena histórico em banco de dados relacional e alerta o usuário via Central de Notificações do macOS.

O objetivo é demonstrar habilidades em:

Web Scraping (Extração de dados da web).

Persistência de Dados (SQL/SQLite).

Integração com Sistema Operacional (Notificações nativas).

Lógica de Negócios (Comparação de preços e tomada de decisão).

🛠 Tecnologias Utilizadas
Linguagem: Python 3.12+

Banco de Dados: SQLite3

Bibliotecas Principais:

requests: Para requisições HTTP com simulação de User-Agent.

BeautifulSoup4: Para parsing e navegação no HTML.

pync: Para integração com notificações do macOS.

📂 Estrutura do Projeto
📦 monitor-precos
 ┣ 📜 main.py        # Controlador principal (Orquestra o fluxo)
 ┣ 📜 scraper.py     # Lógica de extração e limpeza de dados (ETL)
 ┣ 📜 banco.py       # Camada de persistência (CRUD no SQLite)
 ┣ 📜 precos.db      # Arquivo do banco de dados (gerado automaticamente)
 ┗ 📜 README.md      # Documentação
🚀 Como Rodar o Projeto
Pré-requisitos
macOS (devido à biblioteca pync).

Python 3 instalado.

Passo a Passo
Clone o repositório:

Bash

git clone https://github.com/JoaoPaulo121212/monitor-precos.git
cd monitor-precos
Crie e ative um ambiente virtual:

Bash

python3 -m venv .venv
source .venv/bin/activate
Instale as dependências:

Bash

pip install requests beautifulsoup4 pync
Execute o monitor:

Bash

python3 main.py
⚙️ Configuração
Para alterar o produto monitorado, edite as constantes no início do arquivo main.py:

Python

URL_PRODUTO = "http://books.toscrape.com/..."
NOME_PRODUTO = "Seu Produto Aqui"
Nota: O Scraper está configurado com seletores HTML para o site de treino Books to Scrape. Para usar em sites reais (Amazon, Mercado Livre), é necessário ajustar os seletores no arquivo scraper.py e atualizar o User-Agent.
