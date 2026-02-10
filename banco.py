import sqlite3

def iniciar_banco():
    conn = sqlite3.connect('precos.db')
    cursor = conn.cursor()
    # Cria a tabela se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS historico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto TEXT,
            preco REAL,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def salvar_preco(nome, valor):
    conn = sqlite3.connect('precos.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO historico (produto, preco) VALUES (?, ?)', (nome, valor))
    conn.commit()
    conn.close()

def pegar_ultimo_preco(nome):
    conn = sqlite3.connect('precos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT preco FROM historico WHERE produto = ? ORDER BY data DESC LIMIT 1', (nome,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else None