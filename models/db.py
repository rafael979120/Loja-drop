import sqlite3
from config import Config

def get_db_connection():
    # Conecta ao SQLite e configura para retornar linhas como dicionários
    conn = sqlite3.connect(Config.DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    # Cria a tabela de pedidos caso seja a primeira vez rodando o app
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER NOT NULL,
            nome_produto TEXT NOT NULL,
            preco REAL NOT NULL,
            nome_cliente TEXT NOT NULL,
            cpf TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL,
            endereco TEXT NOT NULL,
            status_pagamento TEXT DEFAULT 'pendente',
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            mp_preference_id TEXT
        )
    ''')
    conn.commit()
    conn.close()