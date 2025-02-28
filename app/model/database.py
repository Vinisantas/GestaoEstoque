#Gerencia a conexão com o banco de dados e cria as tabelas necessárias:
import sqlite3
from pathlib import Path

from app.model.Equipamentos_db import inicializar_banco
from app.model.Manutencoes_db import inicializar_banco
from app.model.Movimentacoes_db import inicializar_banco

# Caminho do banco de dados
caminho = "data/equipamentos.sqlite"

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

# Inicializar o banco ao carregar o módulo
inicializar_banco()
