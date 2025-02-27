#Gerencia a conexão com o banco de dados e cria as tabelas necessárias:
import sqlite3
from pathlib import Path

# Caminho do banco de dados
caminho = 'cadastro_patrimonio.sqlite'

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



    # Criar tabela equipamentos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS equipamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patrimonio INTEGER NOT NULL,
        nome TEXT NOT NULL,
        descricao TEXT,
        localizacao TEXT,
        data_de_compra TEXT NOT NULL, 
        FOREIGN KEY (patrimonio) REFERENCES equipamentos (id)
    )
    ''')



    # Criar tabela manutencoes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS manutencoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patrimonio INTEGER NOT NULL,
        descricao TEXT,
        data TEXT NOT NULL,
        FOREIGN KEY (patrimonio) REFERENCES equipamentos (id)
    )
    ''')



    # Criar tabela movimentacoes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movimentacoes (
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
