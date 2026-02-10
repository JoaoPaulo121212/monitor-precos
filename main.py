from pync import notify
from scraper import pegar_preco_produto
from banco import iniciar_banco, salvar_preco, pegar_ultimo_preco
import time

URL_PRODUTO = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
NOME_PRODUTO = "A Light in the Attic"

def check():
    iniciar_banco()
    preco_atual = pegar_preco_produto(URL_PRODUTO)
    ultimo_preco = pegar_ultimo_preco(NOME_PRODUTO)

    if ultimo_preco and preco_atual < ultimo_preco:
        notify(f"O preço caiu para R$ {preco_atual}!", title="🔥 Oportunidade!")
    
    salvar_preco(NOME_PRODUTO, preco_atual)
    print(f"Log: {NOME_PRODUTO} verificado. Preço: {preco_atual}")

# Executa uma vez
check()