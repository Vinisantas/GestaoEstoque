# Caminho do banco de dados
import sqlite3
from pathlib import Path

caminho = "data/manutencoes.sqlite"

def verificar_banco():
    """Verifica se o banco de dados existe e tenta conectar."""
    if not Path(caminho).exists():
        return {"status": "erro", "mensagem": "Banco de dados não encontrado."}
    try:
        conn = sqlite3.connect(caminho)
        conn.close()
        return {"status": "sucesso", "mensagem": "Banco de dados conectado com sucesso."}
    except sqlite3.Error as e:
        return {"status": "erro", "mensagem": f"Erro ao conectar: {e}"}

def inicializar_banco():
    """Cria tabelas no banco de dados, se não existirem."""
    conn = sqlite3.connect(caminho)
    cursor = conn.cursor()

# Criar tabela movimentacoes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS manutencao (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patrimonio INTEGER NOT NULL,
        loja INTEGER NOT NULL,
        data TEXT NOT NULL,
        FOREIGN KEY (patrimonio) REFERENCES equipamentos (id)
    )
    ''')

    conn.commit()
    conn.close()

# Inicializar o banco ao carregar o módulo
inicializar_banco()