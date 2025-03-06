from pathlib import Path
import sqlite3

banco_De_Dados = ["data/equipamentos.sqlite", "data/movimentacoes.sqlite", "data/manutencoes.sqlite"]

def verificar_banco():
    """Verifica se os bancos de dados existem e tenta conectar."""
    resultados = []  # Lista para armazenar os resultados
    for banco in banco_De_Dados:
        if not Path(banco).exists():
            resultados.append ({"status": "erro", "mensagem": f"Banco de dados '{banco}' não encontrado."})
        try:
            conn = sqlite3.connect(banco)
            conn.close()
            resultados.append({"status": "sucesso", "mensagem": f"Banco de dados '{banco}' conectado com sucesso."})
        except sqlite3.Error as e:
            resultados.append ({"status": "erro", "mensagem": f"Erro ao conectar ao banco '{banco}': {e}"})
    return resultados


def inicializar_banco(caminho, tabela_sql):
    """Inicializa o banco de dados, criando tabelas se necessário."""
    Path(caminho).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(caminho)
    cursor = conn.cursor()
    cursor.execute(tabela_sql)
    conn.commit()
    conn.close()