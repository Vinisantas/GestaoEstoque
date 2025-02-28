import sqlite3
import sqlite3
from pathlib import Path



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

def inicializar_banco():
        """Cria tabelas no banco de dados, se não existirem."""
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()


        cursor.execute('''
        CREATE TABLE IF NOT EXISTS equipamentos (
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


# Inserção de dados na tabela equipamentos
def cadastrar_equipamentos(dados):
        try:    
                conn = sqlite3.connect("data/Equipamentos.sqlite")
                cursor = conn.cursor()
                verifica_existencia = cursor.execute(''' SELECT * FROM equipamentos WHERE patrimonio = ? ''', (dados["patrimonio"],)).fetchone()
                if verifica_existencia:
                        return {"status": "erro", "mensagem": "Equipamento já está cadastrado!"}
                else:
                        cursor.execute('''
                                INSERT INTO equipamentos ( patrimonio, nome, descricao, localizacao, data_de_compra)
                                VALUES (?, ?, ?, ?, ?)
                                ''', (dados["patrimonio"], dados["nome"], dados["descricao"], dados["localizacao"], dados["data_de_compra"]))
                
                        conn.commit()
                        conn.close()
                        return {"status": "sucesso", "mensagem": "Equipamento cadastrado com sucesso!"}
        
        except sqlite3.Error as e:

                return {"status": "erro", "mensagem": str(e)}

