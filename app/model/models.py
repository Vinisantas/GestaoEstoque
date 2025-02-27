
import sqlite3
from app.database import verificar_banco

# Inserção de dados na tabela

def cadastrar_equipamentos():
    status_banco = verificar_banco()
    if status_banco ["status"] == "sucesso":
                #defina o caminho do db 
                conn = sqlite3.connect("cadastro_patrimonio.sqlite")
                cursor = conn.cursor()
                cadastro = cursor.execute('''
                        INSERT INTO equipamentos ( patrimonio, nome, descricao, localizacao, data_de_compra)
                        VALUES (?, ?, ?, ?, ?)
                        ''', (patrimonio, nome, descricao, localizacao, data_de_compra))
                
                # Commit e fechamento da conexão
                conn.commit()
                conn.close()
    return cadastro
