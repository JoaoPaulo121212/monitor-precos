import requests
from bs4 import BeautifulSoup

def pegar_preco_produto(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 OPR/126.0.0.0"
    }
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status() # Avisa se der erro 404 ou 500
        res.encoding = 'utf-8'
    except requests.RequestException as e:
        print(f"Erro ao acessar o site: {e}")
        return 0.0

    soup = BeautifulSoup(res.text, 'html.parser')
    
    elemento_preco = soup.find("p", class_="price_color")
    
    if elemento_preco:
        preco_texto = elemento_preco.get_text()
        
        preco_limpo_str = preco_texto.replace('£', '').replace('Â', '').strip()
        
        try:
            preco_limpo = float(preco_limpo_str)
            return preco_limpo
        except ValueError:
            print(f"Não consegui converter '{preco_texto}' para número.")
            return 0.0
    else:
        print("Não encontrei a tag de preço no site.")
        return 0.0